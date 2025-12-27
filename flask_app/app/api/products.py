"""商品API"""
from flask import request
from app.api import api_bp
from app import db
from app.models_product import Product, Category
from app.utils import token_required, admin_required, success_response, error_response, paginate_query

# 分类管理
@api_bp.route('/categories', methods=['GET'])
def get_categories():
    """获取所有分类"""
    categories = Category.query.all()
    return success_response([c.to_dict() for c in categories])

@api_bp.route('/categories', methods=['POST'])
@admin_required
def create_category(current_user):
    """创建分类（管理员）"""
    data = request.get_json()
    name = data.get('name', '').strip()
    
    if not name:
        return error_response('分类名称不能为空')
    
    if Category.query.filter_by(name=name).first():
        return error_response('分类已存在')
    
    category = Category(name=name, description=data.get('description', ''))
    db.session.add(category)
    db.session.commit()
    
    return success_response(category.to_dict(), '创建成功', 201)

@api_bp.route('/categories/<int:category_id>', methods=['PUT'])
@admin_required
def update_category(current_user, category_id):
    """更新分类（管理员）"""
    category = Category.query.get_or_404(category_id)
    data = request.get_json()
    
    if 'name' in data:
        name = data['name'].strip()
        if Category.query.filter(Category.name == name, Category.id != category_id).first():
            return error_response('分类名称已存在')
        category.name = name
    
    if 'description' in data:
        category.description = data['description']
    
    db.session.commit()
    return success_response(category.to_dict(), '更新成功')

@api_bp.route('/categories/<int:category_id>', methods=['DELETE'])
@admin_required
def delete_category(current_user, category_id):
    """删除分类（管理员）"""
    category = Category.query.get_or_404(category_id)
    
    if category.products.count() > 0:
        return error_response('该分类下有商品，无法删除')
    
    db.session.delete(category)
    db.session.commit()
    return success_response(message='删除成功')

# 商品管理
@api_bp.route('/products', methods=['GET'])
def get_products():
    """获取商品列表"""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    category_id = request.args.get('category_id', type=int)
    keyword = request.args.get('keyword', '').strip()
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)
    sort_by = request.args.get('sort_by', 'created_at')
    sort_order = request.args.get('sort_order', 'desc')
    
    query = Product.query.filter_by(is_active=True)
    
    if category_id:
        query = query.filter_by(category_id=category_id)
    
    if keyword:
        query = query.filter(Product.name.contains(keyword))
    
    if min_price is not None:
        query = query.filter(Product.price >= min_price)
    
    if max_price is not None:
        query = query.filter(Product.price <= max_price)
    
    # 排序
    sort_column = getattr(Product, sort_by, Product.created_at)
    if sort_order == 'asc':
        query = query.order_by(sort_column.asc())
    else:
        query = query.order_by(sort_column.desc())
    
    result = paginate_query(query, page, per_page)
    return success_response(result)

@api_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """获取商品详情"""
    product = Product.query.get_or_404(product_id)
    return success_response(product.to_dict())

@api_bp.route('/products', methods=['POST'])
@admin_required
def create_product(current_user):
    """创建商品（管理员）"""
    data = request.get_json()
    
    name = data.get('name', '').strip()
    price = data.get('price')
    
    if not name:
        return error_response('商品名称不能为空')
    
    if price is None or price < 0:
        return error_response('价格无效')
    
    product = Product(
        name=name,
        description=data.get('description', ''),
        price=price,
        stock=data.get('stock', 0),
        category_id=data.get('category_id'),
        image_url=data.get('image_url', '')
    )
    
    db.session.add(product)
    db.session.commit()
    
    return success_response(product.to_dict(), '创建成功', 201)

@api_bp.route('/products/<int:product_id>', methods=['PUT'])
@admin_required
def update_product(current_user, product_id):
    """更新商品（管理员）"""
    product = Product.query.get_or_404(product_id)
    data = request.get_json()
    
    if 'name' in data:
        product.name = data['name'].strip()
    if 'description' in data:
        product.description = data['description']
    if 'price' in data:
        if data['price'] < 0:
            return error_response('价格无效')
        product.price = data['price']
    if 'stock' in data:
        if data['stock'] < 0:
            return error_response('库存无效')
        product.stock = data['stock']
    if 'category_id' in data:
        product.category_id = data['category_id']
    if 'image_url' in data:
        product.image_url = data['image_url']
    if 'is_active' in data:
        product.is_active = bool(data['is_active'])
    
    db.session.commit()
    return success_response(product.to_dict(), '更新成功')

@api_bp.route('/products/<int:product_id>', methods=['DELETE'])
@admin_required
def delete_product(current_user, product_id):
    """删除商品（管理员）"""
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return success_response(message='删除成功')

# 库存管理
@api_bp.route('/products/<int:product_id>/stock', methods=['PUT'])
@admin_required
def update_stock(current_user, product_id):
    """更新库存（管理员）"""
    product = Product.query.get_or_404(product_id)
    data = request.get_json()
    
    action = data.get('action')  # add, subtract, set
    quantity = data.get('quantity', 0)
    
    if action == 'add':
        product.stock += quantity
    elif action == 'subtract':
        if product.stock < quantity:
            return error_response('库存不足')
        product.stock -= quantity
    elif action == 'set':
        if quantity < 0:
            return error_response('库存不能为负数')
        product.stock = quantity
    else:
        return error_response('无效的操作')
    
    db.session.commit()
    return success_response({'stock': product.stock}, '库存更新成功')
