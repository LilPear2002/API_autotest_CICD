"""订单API"""
from flask import request
from app.api import api_bp
from app import db
from app.models_product import Product, CartItem, Order, OrderItem
from app.utils import token_required, admin_required, success_response, error_response, paginate_query
import uuid
from datetime import datetime

# 购物车
@api_bp.route('/cart', methods=['GET'])
@token_required
def get_cart(current_user):
    """获取购物车"""
    items = CartItem.query.filter_by(user_id=current_user.id).all()
    total = sum(item.product.price * item.quantity for item in items)
    return success_response({
        'items': [item.to_dict() for item in items],
        'total': total
    })

@api_bp.route('/cart', methods=['POST'])
@token_required
def add_to_cart(current_user):
    """添加商品到购物车"""
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)
    
    if not product_id:
        return error_response('商品ID不能为空')
    
    product = Product.query.get_or_404(product_id)
    
    if not product.is_active:
        return error_response('商品已下架')
    
    if product.stock < quantity:
        return error_response('库存不足')
    
    cart_item = CartItem.query.filter_by(user_id=current_user.id, product_id=product_id).first()
    
    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = CartItem(user_id=current_user.id, product_id=product_id, quantity=quantity)
        db.session.add(cart_item)
    
    db.session.commit()
    return success_response(cart_item.to_dict(), '添加成功')

@api_bp.route('/cart/<int:item_id>', methods=['PUT'])
@token_required
def update_cart_item(current_user, item_id):
    """更新购物车项"""
    cart_item = CartItem.query.filter_by(id=item_id, user_id=current_user.id).first_or_404()
    data = request.get_json()
    quantity = data.get('quantity', 1)
    
    if quantity <= 0:
        db.session.delete(cart_item)
    else:
        if cart_item.product.stock < quantity:
            return error_response('库存不足')
        cart_item.quantity = quantity
    
    db.session.commit()
    return success_response(message='更新成功')

@api_bp.route('/cart/<int:item_id>', methods=['DELETE'])
@token_required
def remove_from_cart(current_user, item_id):
    """从购物车移除商品"""
    cart_item = CartItem.query.filter_by(id=item_id, user_id=current_user.id).first_or_404()
    db.session.delete(cart_item)
    db.session.commit()
    return success_response(message='删除成功')

@api_bp.route('/cart/clear', methods=['DELETE'])
@token_required
def clear_cart(current_user):
    """清空购物车"""
    CartItem.query.filter_by(user_id=current_user.id).delete()
    db.session.commit()
    return success_response(message='购物车已清空')

# 订单
@api_bp.route('/orders', methods=['GET'])
@token_required
def get_orders(current_user):
    """获取订单列表"""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    status = request.args.get('status')
    
    query = Order.query.filter_by(user_id=current_user.id)
    
    if status:
        query = query.filter_by(status=status)
    
    query = query.order_by(Order.created_at.desc())
    result = paginate_query(query, page, per_page)
    return success_response(result)

@api_bp.route('/orders/<int:order_id>', methods=['GET'])
@token_required
def get_order(current_user, order_id):
    """获取订单详情"""
    order = Order.query.filter_by(id=order_id, user_id=current_user.id).first_or_404()
    return success_response(order.to_dict())

@api_bp.route('/orders', methods=['POST'])
@token_required
def create_order(current_user):
    """创建订单"""
    data = request.get_json()
    shipping_address = data.get('shipping_address', '').strip()
    
    if not shipping_address:
        return error_response('收货地址不能为空')
    
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    
    if not cart_items:
        return error_response('购物车为空')
    
    # 检查库存
    for item in cart_items:
        if item.product.stock < item.quantity:
            return error_response(f'商品 {item.product.name} 库存不足')
    
    # 创建订单
    order_no = f"ORD{datetime.now().strftime('%Y%m%d%H%M%S')}{uuid.uuid4().hex[:6].upper()}"
    total_amount = sum(item.product.price * item.quantity for item in cart_items)
    
    order = Order(
        order_no=order_no,
        user_id=current_user.id,
        total_amount=total_amount,
        shipping_address=shipping_address
    )
    db.session.add(order)
    db.session.flush()
    
    # 创建订单项并扣减库存
    for item in cart_items:
        order_item = OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            product_name=item.product.name,
            price=item.product.price,
            quantity=item.quantity
        )
        db.session.add(order_item)
        item.product.stock -= item.quantity
    
    # 清空购物车
    CartItem.query.filter_by(user_id=current_user.id).delete()
    
    db.session.commit()
    return success_response(order.to_dict(), '订单创建成功', 201)

@api_bp.route('/orders/<int:order_id>/pay', methods=['POST'])
@token_required
def pay_order(current_user, order_id):
    """支付订单"""
    order = Order.query.filter_by(id=order_id, user_id=current_user.id).first_or_404()
    
    if order.status != 'pending':
        return error_response('订单状态不允许支付')
    
    data = request.get_json()
    payment_method = data.get('payment_method', 'alipay')
    
    # 模拟支付成功
    order.status = 'paid'
    order.payment_method = payment_method
    db.session.commit()
    
    return success_response(order.to_dict(), '支付成功')

@api_bp.route('/orders/<int:order_id>/cancel', methods=['POST'])
@token_required
def cancel_order(current_user, order_id):
    """取消订单"""
    order = Order.query.filter_by(id=order_id, user_id=current_user.id).first_or_404()
    
    if order.status not in ['pending', 'paid']:
        return error_response('订单状态不允许取消')
    
    # 恢复库存
    for item in order.items:
        if item.product:
            item.product.stock += item.quantity
    
    order.status = 'cancelled'
    db.session.commit()
    
    return success_response(order.to_dict(), '订单已取消')

@api_bp.route('/orders/<int:order_id>/refund', methods=['POST'])
@token_required
def refund_order(current_user, order_id):
    """申请退款"""
    order = Order.query.filter_by(id=order_id, user_id=current_user.id).first_or_404()
    
    if order.status != 'paid':
        return error_response('只有已支付的订单可以申请退款')
    
    # 恢复库存
    for item in order.items:
        if item.product:
            item.product.stock += item.quantity
    
    order.status = 'refunded'
    db.session.commit()
    
    return success_response(order.to_dict(), '退款成功')

# 管理员订单管理
@api_bp.route('/admin/orders', methods=['GET'])
@admin_required
def admin_get_orders(current_user):
    """获取所有订单（管理员）"""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    status = request.args.get('status')
    user_id = request.args.get('user_id', type=int)
    
    query = Order.query
    
    if status:
        query = query.filter_by(status=status)
    if user_id:
        query = query.filter_by(user_id=user_id)
    
    query = query.order_by(Order.created_at.desc())
    result = paginate_query(query, page, per_page)
    return success_response(result)

@api_bp.route('/admin/orders/<int:order_id>/status', methods=['PUT'])
@admin_required
def admin_update_order_status(current_user, order_id):
    """更新订单状态（管理员）"""
    order = Order.query.get_or_404(order_id)
    data = request.get_json()
    status = data.get('status')
    
    valid_statuses = ['pending', 'paid', 'shipped', 'completed', 'cancelled', 'refunded']
    if status not in valid_statuses:
        return error_response('无效的订单状态')
    
    order.status = status
    db.session.commit()
    
    return success_response(order.to_dict(), '状态更新成功')
