"""数据查询API"""
from flask import request
from app.api import api_bp
from app import db
from app.models_product import Product, Order, Category
from app.models import User
from app.utils import admin_required, success_response, error_response
from sqlalchemy import func

@api_bp.route('/query/products', methods=['GET'])
def query_products():
    """高级商品查询"""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    # 筛选条件
    category_id = request.args.get('category_id', type=int)
    keyword = request.args.get('keyword', '').strip()
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)
    in_stock = request.args.get('in_stock')  # true/false
    
    # 排序
    sort_by = request.args.get('sort_by', 'created_at')
    sort_order = request.args.get('sort_order', 'desc')
    
    query = Product.query.filter_by(is_active=True)
    
    # 应用筛选
    if category_id:
        query = query.filter_by(category_id=category_id)
    if keyword:
        query = query.filter(
            db.or_(
                Product.name.contains(keyword),
                Product.description.contains(keyword)
            )
        )
    if min_price is not None:
        query = query.filter(Product.price >= min_price)
    if max_price is not None:
        query = query.filter(Product.price <= max_price)
    if in_stock == 'true':
        query = query.filter(Product.stock > 0)
    elif in_stock == 'false':
        query = query.filter(Product.stock == 0)
    
    # 应用排序
    valid_sort_fields = ['name', 'price', 'stock', 'created_at']
    if sort_by in valid_sort_fields:
        sort_column = getattr(Product, sort_by)
        if sort_order == 'asc':
            query = query.order_by(sort_column.asc())
        else:
            query = query.order_by(sort_column.desc())
    
    # 分页
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    
    return success_response({
        'items': [p.to_dict() for p in pagination.items],
        'total': pagination.total,
        'pages': pagination.pages,
        'current_page': page,
        'per_page': per_page,
        'has_next': pagination.has_next,
        'has_prev': pagination.has_prev
    })

@api_bp.route('/query/stats', methods=['GET'])
@admin_required
def get_stats(current_user):
    """获取统计数据（管理员）"""
    # 用户统计
    total_users = User.query.count()
    active_users = User.query.filter_by(is_active=True).count()
    
    # 商品统计
    total_products = Product.query.count()
    active_products = Product.query.filter_by(is_active=True).count()
    out_of_stock = Product.query.filter(Product.stock == 0, Product.is_active == True).count()
    
    # 订单统计
    total_orders = Order.query.count()
    order_stats = db.session.query(
        Order.status,
        func.count(Order.id).label('count'),
        func.sum(Order.total_amount).label('amount')
    ).group_by(Order.status).all()
    
    order_by_status = {
        stat.status: {'count': stat.count, 'amount': float(stat.amount or 0)}
        for stat in order_stats
    }
    
    # 销售额
    total_revenue = db.session.query(
        func.sum(Order.total_amount)
    ).filter(Order.status.in_(['paid', 'shipped', 'completed'])).scalar() or 0
    
    # 分类商品数量
    category_stats = db.session.query(
        Category.name,
        func.count(Product.id).label('count')
    ).outerjoin(Product).group_by(Category.id).all()
    
    return success_response({
        'users': {
            'total': total_users,
            'active': active_users
        },
        'products': {
            'total': total_products,
            'active': active_products,
            'out_of_stock': out_of_stock
        },
        'orders': {
            'total': total_orders,
            'by_status': order_by_status
        },
        'revenue': float(total_revenue),
        'categories': [{'name': c.name, 'product_count': c.count} for c in category_stats]
    })

@api_bp.route('/query/orders/aggregate', methods=['GET'])
@admin_required
def aggregate_orders(current_user):
    """订单聚合查询（管理员）"""
    group_by = request.args.get('group_by', 'day')  # day, month, status
    
    if group_by == 'day':
        results = db.session.query(
            func.date(Order.created_at).label('date'),
            func.count(Order.id).label('count'),
            func.sum(Order.total_amount).label('amount')
        ).group_by(func.date(Order.created_at)).order_by(func.date(Order.created_at).desc()).limit(30).all()
        
        data = [{'date': str(r.date), 'count': r.count, 'amount': float(r.amount or 0)} for r in results]
    
    elif group_by == 'month':
        results = db.session.query(
            func.strftime('%Y-%m', Order.created_at).label('month'),
            func.count(Order.id).label('count'),
            func.sum(Order.total_amount).label('amount')
        ).group_by(func.strftime('%Y-%m', Order.created_at)).order_by(func.strftime('%Y-%m', Order.created_at).desc()).limit(12).all()
        
        data = [{'month': r.month, 'count': r.count, 'amount': float(r.amount or 0)} for r in results]
    
    elif group_by == 'status':
        results = db.session.query(
            Order.status,
            func.count(Order.id).label('count'),
            func.sum(Order.total_amount).label('amount')
        ).group_by(Order.status).all()
        
        data = [{'status': r.status, 'count': r.count, 'amount': float(r.amount or 0)} for r in results]
    
    else:
        return error_response('无效的分组方式')
    
    return success_response(data)

@api_bp.route('/query/products/top', methods=['GET'])
@admin_required
def top_products(current_user):
    """热销商品排行（管理员）"""
    from app.models_product import OrderItem
    
    limit = request.args.get('limit', 10, type=int)
    
    results = db.session.query(
        Product.id,
        Product.name,
        func.sum(OrderItem.quantity).label('sold_count'),
        func.sum(OrderItem.price * OrderItem.quantity).label('revenue')
    ).join(OrderItem, Product.id == OrderItem.product_id
    ).join(Order, OrderItem.order_id == Order.id
    ).filter(Order.status.in_(['paid', 'shipped', 'completed'])
    ).group_by(Product.id
    ).order_by(func.sum(OrderItem.quantity).desc()
    ).limit(limit).all()
    
    return success_response([{
        'id': r.id,
        'name': r.name,
        'sold_count': int(r.sold_count or 0),
        'revenue': float(r.revenue or 0)
    } for r in results])
