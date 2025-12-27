"""视图蓝图"""
from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from functools import wraps

main_bp = Blueprint('main', __name__)

def login_required(f):
    """登录验证装饰器"""
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            flash('请先登录', 'warning')
            return redirect(url_for('main.login'))
        return f(*args, **kwargs)
    return decorated

def admin_required(f):
    """管理员验证装饰器"""
    @wraps(f)
    @login_required
    def decorated(*args, **kwargs):
        if session.get('role') != 'admin':
            flash('需要管理员权限', 'danger')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated

@main_bp.route('/')
def index():
    """首页"""
    from app.models_product import Product, Category
    categories = Category.query.all()
    products = Product.query.filter_by(is_active=True).order_by(Product.created_at.desc()).limit(8).all()
    return render_template('index.html', categories=categories, products=products)

@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    """注册页面"""
    if request.method == 'POST':
        from app.models import User
        from app import db
        import re
        
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        
        if not username or not email or not password:
            flash('请填写所有字段', 'danger')
            return render_template('register.html')
        
        if len(password) < 6:
            flash('密码至少6个字符', 'danger')
            return render_template('register.html')
        
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            flash('邮箱格式不正确', 'danger')
            return render_template('register.html')
        
        if User.query.filter_by(username=username).first():
            flash('用户名已存在', 'danger')
            return render_template('register.html')
        
        if User.query.filter_by(email=email).first():
            flash('邮箱已被注册', 'danger')
            return render_template('register.html')
        
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('注册成功，请登录', 'success')
        return redirect(url_for('main.login'))
    
    return render_template('register.html')

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    """登录页面"""
    if request.method == 'POST':
        from app.models import User
        
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        
        user = User.query.filter_by(username=username).first()
        
        if not user or not user.check_password(password):
            flash('用户名或密码错误', 'danger')
            return render_template('login.html')
        
        if not user.is_active:
            flash('用户已被禁用', 'danger')
            return render_template('login.html')
        
        session['user_id'] = user.id
        session['username'] = user.username
        session['role'] = user.role
        session['token'] = user.generate_token()
        
        flash('登录成功', 'success')
        return redirect(url_for('main.index'))
    
    return render_template('login.html')

@main_bp.route('/logout')
def logout():
    """登出"""
    session.clear()
    flash('已登出', 'info')
    return redirect(url_for('main.index'))

@main_bp.route('/products')
def products():
    """商品列表"""
    from app.models_product import Product, Category
    
    page = request.args.get('page', 1, type=int)
    category_id = request.args.get('category_id', type=int)
    keyword = request.args.get('keyword', '').strip()
    
    query = Product.query.filter_by(is_active=True)
    
    if category_id:
        query = query.filter_by(category_id=category_id)
    if keyword:
        query = query.filter(Product.name.contains(keyword))
    
    pagination = query.order_by(Product.created_at.desc()).paginate(page=page, per_page=12, error_out=False)
    categories = Category.query.all()
    
    return render_template('products.html', 
                          products=pagination.items, 
                          pagination=pagination,
                          categories=categories,
                          current_category=category_id,
                          keyword=keyword)

@main_bp.route('/products/<int:product_id>')
def product_detail(product_id):
    """商品详情"""
    from app.models_product import Product
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)

@main_bp.route('/cart')
@login_required
def cart():
    """购物车"""
    from app.models_product import CartItem
    items = CartItem.query.filter_by(user_id=session['user_id']).all()
    total = sum(item.product.price * item.quantity for item in items)
    return render_template('cart.html', items=items, total=total)

@main_bp.route('/orders')
@login_required
def orders():
    """订单列表"""
    from app.models_product import Order
    page = request.args.get('page', 1, type=int)
    pagination = Order.query.filter_by(user_id=session['user_id']).order_by(Order.created_at.desc()).paginate(page=page, per_page=10, error_out=False)
    return render_template('orders.html', orders=pagination.items, pagination=pagination)

@main_bp.route('/orders/<int:order_id>')
@login_required
def order_detail(order_id):
    """订单详情"""
    from app.models_product import Order
    order = Order.query.filter_by(id=order_id, user_id=session['user_id']).first_or_404()
    return render_template('order_detail.html', order=order)

@main_bp.route('/profile')
@login_required
def profile():
    """个人中心"""
    from app.models import User
    user = User.query.get(session['user_id'])
    return render_template('profile.html', user=user)

@main_bp.route('/files')
@login_required
def files():
    """文件管理"""
    from app.models_file import File
    page = request.args.get('page', 1, type=int)
    pagination = File.query.filter_by(user_id=session['user_id']).order_by(File.upload_at.desc()).paginate(page=page, per_page=10, error_out=False)
    return render_template('files.html', files=pagination.items, pagination=pagination)

# 管理后台
@main_bp.route('/admin')
@admin_required
def admin_dashboard():
    """管理后台首页"""
    from app.models import User
    from app.models_product import Product, Order, Category
    
    stats = {
        'users': User.query.count(),
        'products': Product.query.count(),
        'orders': Order.query.count(),
        'categories': Category.query.count()
    }
    recent_orders = Order.query.order_by(Order.created_at.desc()).limit(5).all()
    return render_template('admin/dashboard.html', stats=stats, recent_orders=recent_orders)

@main_bp.route('/admin/users')
@admin_required
def admin_users():
    """用户管理"""
    from app.models import User
    page = request.args.get('page', 1, type=int)
    pagination = User.query.order_by(User.created_at.desc()).paginate(page=page, per_page=10, error_out=False)
    return render_template('admin/users.html', users=pagination.items, pagination=pagination)

@main_bp.route('/admin/products')
@admin_required
def admin_products():
    """商品管理"""
    from app.models_product import Product, Category
    page = request.args.get('page', 1, type=int)
    pagination = Product.query.order_by(Product.created_at.desc()).paginate(page=page, per_page=10, error_out=False)
    categories = Category.query.all()
    return render_template('admin/products.html', products=pagination.items, pagination=pagination, categories=categories)

@main_bp.route('/admin/orders')
@admin_required
def admin_orders():
    """订单管理"""
    from app.models_product import Order
    page = request.args.get('page', 1, type=int)
    status = request.args.get('status')
    
    query = Order.query
    if status:
        query = query.filter_by(status=status)
    
    pagination = query.order_by(Order.created_at.desc()).paginate(page=page, per_page=10, error_out=False)
    return render_template('admin/orders.html', orders=pagination.items, pagination=pagination, current_status=status)

@main_bp.route('/admin/categories')
@admin_required
def admin_categories():
    """分类管理"""
    from app.models_product import Category
    categories = Category.query.all()
    return render_template('admin/categories.html', categories=categories)
