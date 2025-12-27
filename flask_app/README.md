# Flask商城 - 接口自动化测试练习项目

一个完整的Flask Web应用，专为接口自动化测试和Web自动化测试练习设计。

## 功能模块

- **用户系统**: 注册、登录、登出、JWT认证、角色权限(管理员/普通用户)
- **商品订单**: 商品CRUD、分类管理、购物车、订单(创建/支付/取消/退款)、库存管理
- **文件管理**: 文件上传、下载、列表、删除
- **数据查询**: 分页、筛选、排序、聚合统计

## 技术栈

- Flask 3.0 + Flask-SQLAlchemy + Flask-RESTful
- JWT认证 (PyJWT)
- SQLite数据库
- Bootstrap 5 前端
- Jinja2模板

## 快速开始

```bash
# 1. 进入项目目录
cd flask_app

# 2. 创建虚拟环境
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# 3. 安装依赖
pip install -r requirements.txt

# 4. 初始化测试数据
python init_data.py

# 5. 启动应用
python run.py
```

访问 http://localhost:5000

## 测试账号

| 角色 | 用户名 | 密码 |
|------|--------|------|
| 管理员 | admin | admin123 |
| 普通用户 | testuser | test123 |

## 文档

- [API文档](docs/API_DOCUMENT.md) - 完整的RESTful API接口文档
- [元素定位文档](docs/ELEMENT_LOCATOR.md) - Web自动化测试元素定位

## 项目结构

```
flask_app/
├── app/
│   ├── api/           # RESTful API
│   ├── templates/     # Jinja2模板
│   ├── views/         # 视图路由
│   ├── models.py      # 用户模型
│   ├── models_product.py  # 商品订单模型
│   ├── models_file.py # 文件模型
│   └── utils.py       # 工具函数
├── docs/              # 文档
├── config.py          # 配置
├── run.py             # 入口
└── init_data.py       # 初始化数据
```
