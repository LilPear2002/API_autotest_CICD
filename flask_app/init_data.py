"""初始化测试数据"""
from app import create_app, db
from app.models import User
from app.models_product import Category, Product

app = create_app()

with app.app_context():
    # 创建分类
    categories_data = [
        {'name': '电子产品', 'description': '手机、电脑、数码产品'},
        {'name': '服装鞋帽', 'description': '男装、女装、鞋子、帽子'},
        {'name': '食品饮料', 'description': '零食、饮料、生鲜'},
        {'name': '家居用品', 'description': '家具、装饰、日用品'},
        {'name': '图书文具', 'description': '书籍、文具、办公用品'}
    ]
    
    for cat_data in categories_data:
        if not Category.query.filter_by(name=cat_data['name']).first():
            category = Category(**cat_data)
            db.session.add(category)
    
    db.session.commit()
    
    # 获取分类
    electronics = Category.query.filter_by(name='电子产品').first()
    clothing = Category.query.filter_by(name='服装鞋帽').first()
    food = Category.query.filter_by(name='食品饮料').first()
    home = Category.query.filter_by(name='家居用品').first()
    books = Category.query.filter_by(name='图书文具').first()
    
    # 创建商品
    products_data = [
        {'name': 'iPhone 15', 'description': '苹果最新款手机', 'price': 6999.00, 'stock': 100, 'category_id': electronics.id},
        {'name': 'MacBook Pro', 'description': '苹果笔记本电脑', 'price': 12999.00, 'stock': 50, 'category_id': electronics.id},
        {'name': 'AirPods Pro', 'description': '苹果无线耳机', 'price': 1999.00, 'stock': 200, 'category_id': electronics.id},
        {'name': '华为Mate 60', 'description': '华为旗舰手机', 'price': 5999.00, 'stock': 80, 'category_id': electronics.id},
        {'name': '小米14', 'description': '小米旗舰手机', 'price': 3999.00, 'stock': 150, 'category_id': electronics.id},
        {'name': '男士休闲T恤', 'description': '纯棉舒适T恤', 'price': 99.00, 'stock': 500, 'category_id': clothing.id},
        {'name': '女士连衣裙', 'description': '夏季清凉连衣裙', 'price': 199.00, 'stock': 300, 'category_id': clothing.id},
        {'name': '运动鞋', 'description': '透气跑步鞋', 'price': 399.00, 'stock': 200, 'category_id': clothing.id},
        {'name': '牛仔裤', 'description': '经典直筒牛仔裤', 'price': 259.00, 'stock': 400, 'category_id': clothing.id},
        {'name': '进口零食大礼包', 'description': '多种进口零食组合', 'price': 128.00, 'stock': 1000, 'category_id': food.id},
        {'name': '有机牛奶', 'description': '新鲜有机纯牛奶', 'price': 68.00, 'stock': 500, 'category_id': food.id},
        {'name': '咖啡豆', 'description': '进口阿拉比卡咖啡豆', 'price': 88.00, 'stock': 300, 'category_id': food.id},
        {'name': '简约沙发', 'description': '北欧风格三人沙发', 'price': 2999.00, 'stock': 30, 'category_id': home.id},
        {'name': '台灯', 'description': 'LED护眼台灯', 'price': 159.00, 'stock': 200, 'category_id': home.id},
        {'name': '收纳盒套装', 'description': '多功能收纳盒', 'price': 49.00, 'stock': 800, 'category_id': home.id},
        {'name': 'Python编程入门', 'description': 'Python基础教程', 'price': 59.00, 'stock': 500, 'category_id': books.id},
        {'name': '软件测试实战', 'description': '自动化测试指南', 'price': 79.00, 'stock': 300, 'category_id': books.id},
        {'name': '中性笔套装', 'description': '12支装中性笔', 'price': 19.90, 'stock': 1000, 'category_id': books.id},
    ]
    
    for prod_data in products_data:
        if not Product.query.filter_by(name=prod_data['name']).first():
            product = Product(**prod_data)
            db.session.add(product)
    
    db.session.commit()
    
    # 创建测试用户
    if not User.query.filter_by(username='testuser').first():
        user = User(username='testuser', email='test@example.com')
        user.set_password('test123')
        db.session.add(user)
        db.session.commit()
    
    print('测试数据初始化完成！')
    print('管理员账号: admin / admin123')
    print('测试用户: testuser / test123')
