# Flask商城 API文档

## 基础信息

- **Base URL**: `http://localhost:5000/api`
- **认证方式**: JWT Token (Bearer Token)
- **请求头**: `Authorization: Bearer <token>`

## 响应格式

```json
{
    "code": 200,
    "message": "操作成功",
    "data": {}
}
```

---

## 1. 用户认证模块

### 1.1 用户注册

**POST** `/auth/register`

**请求体**:
```json
{
    "username": "testuser",
    "email": "test@example.com",
    "password": "123456"
}
```

**响应**:
```json
{
    "code": 201,
    "message": "注册成功",
    "data": {
        "id": 1,
        "username": "testuser",
        "email": "test@example.com",
        "role": "user",
        "created_at": "2024-01-01T00:00:00",
        "is_active": true
    }
}
```

**错误码**:
- 400: 参数验证失败（用户名/邮箱已存在、格式错误等）

---

### 1.2 用户登录

**POST** `/auth/login`

**请求体**:
```json
{
    "username": "testuser",
    "password": "123456"
}
```

**响应**:
```json
{
    "code": 200,
    "message": "登录成功",
    "data": {
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
        "user": {
            "id": 1,
            "username": "testuser",
            "email": "test@example.com",
            "role": "user"
        }
    }
}
```

**错误码**:
- 401: 用户名或密码错误
- 403: 用户已被禁用

---

### 1.3 用户登出

**POST** `/auth/logout`

**需要认证**: 是

**响应**:
```json
{
    "code": 200,
    "message": "登出成功",
    "data": null
}
```

---

### 1.4 获取当前用户信息

**GET** `/auth/profile`

**需要认证**: 是

**响应**:
```json
{
    "code": 200,
    "message": "操作成功",
    "data": {
        "id": 1,
        "username": "testuser",
        "email": "test@example.com",
        "role": "user",
        "created_at": "2024-01-01T00:00:00",
        "is_active": true
    }
}
```

---

### 1.5 更新用户信息

**PUT** `/auth/profile`

**需要认证**: 是

**请求体**:
```json
{
    "email": "newemail@example.com"
}
```

**响应**:
```json
{
    "code": 200,
    "message": "更新成功",
    "data": {
        "id": 1,
        "username": "testuser",
        "email": "newemail@example.com"
    }
}
```

---

### 1.6 修改密码

**PUT** `/auth/password`

**需要认证**: 是

**请求体**:
```json
{
    "old_password": "123456",
    "new_password": "654321"
}
```

**响应**:
```json
{
    "code": 200,
    "message": "密码修改成功",
    "data": null
}
```

---

## 2. 商品模块

### 2.1 获取分类列表

**GET** `/categories`

**需要认证**: 否

**响应**:
```json
{
    "code": 200,
    "message": "操作成功",
    "data": [
        {"id": 1, "name": "电子产品", "description": "手机、电脑等"},
        {"id": 2, "name": "服装鞋帽", "description": "男装、女装等"}
    ]
}
```

---

### 2.2 创建分类（管理员）

**POST** `/categories`

**需要认证**: 是（管理员）

**请求体**:
```json
{
    "name": "新分类",
    "description": "分类描述"
}
```

---

### 2.3 更新分类（管理员）

**PUT** `/categories/<category_id>`

**需要认证**: 是（管理员）

**请求体**:
```json
{
    "name": "更新后的名称",
    "description": "更新后的描述"
}
```

---

### 2.4 删除分类（管理员）

**DELETE** `/categories/<category_id>`

**需要认证**: 是（管理员）

---

### 2.5 获取商品列表

**GET** `/products`

**需要认证**: 否

**查询参数**:
| 参数 | 类型 | 说明 |
|------|------|------|
| page | int | 页码，默认1 |
| per_page | int | 每页数量，默认10 |
| category_id | int | 分类ID |
| keyword | string | 搜索关键词 |
| min_price | float | 最低价格 |
| max_price | float | 最高价格 |
| sort_by | string | 排序字段(name/price/stock/created_at) |
| sort_order | string | 排序方式(asc/desc) |

**响应**:
```json
{
    "code": 200,
    "message": "操作成功",
    "data": {
        "items": [
            {
                "id": 1,
                "name": "iPhone 15",
                "description": "苹果最新款手机",
                "price": 6999.00,
                "stock": 100,
                "category_id": 1,
                "category_name": "电子产品",
                "is_active": true,
                "created_at": "2024-01-01T00:00:00"
            }
        ],
        "total": 100,
        "pages": 10,
        "current_page": 1,
        "per_page": 10,
        "has_next": true,
        "has_prev": false
    }
}
```

---

### 2.6 获取商品详情

**GET** `/products/<product_id>`

**需要认证**: 否

---

### 2.7 创建商品（管理员）

**POST** `/products`

**需要认证**: 是（管理员）

**请求体**:
```json
{
    "name": "新商品",
    "description": "商品描述",
    "price": 99.99,
    "stock": 100,
    "category_id": 1,
    "image_url": "http://example.com/image.jpg"
}
```

---

### 2.8 更新商品（管理员）

**PUT** `/products/<product_id>`

**需要认证**: 是（管理员）

**请求体**:
```json
{
    "name": "更新后的名称",
    "price": 199.99,
    "stock": 50,
    "is_active": true
}
```

---

### 2.9 删除商品（管理员）

**DELETE** `/products/<product_id>`

**需要认证**: 是（管理员）

---

### 2.10 更新库存（管理员）

**PUT** `/products/<product_id>/stock`

**需要认证**: 是（管理员）

**请求体**:
```json
{
    "action": "add",  // add, subtract, set
    "quantity": 10
}
```

---

## 3. 购物车模块

### 3.1 获取购物车

**GET** `/cart`

**需要认证**: 是

**响应**:
```json
{
    "code": 200,
    "message": "操作成功",
    "data": {
        "items": [
            {
                "id": 1,
                "product_id": 1,
                "product_name": "iPhone 15",
                "price": 6999.00,
                "quantity": 2,
                "subtotal": 13998.00
            }
        ],
        "total": 13998.00
    }
}
```

---

### 3.2 添加商品到购物车

**POST** `/cart`

**需要认证**: 是

**请求体**:
```json
{
    "product_id": 1,
    "quantity": 1
}
```

---

### 3.3 更新购物车项

**PUT** `/cart/<item_id>`

**需要认证**: 是

**请求体**:
```json
{
    "quantity": 3
}
```

---

### 3.4 删除购物车项

**DELETE** `/cart/<item_id>`

**需要认证**: 是

---

### 3.5 清空购物车

**DELETE** `/cart/clear`

**需要认证**: 是

---

## 4. 订单模块

### 4.1 获取订单列表

**GET** `/orders`

**需要认证**: 是

**查询参数**:
| 参数 | 类型 | 说明 |
|------|------|------|
| page | int | 页码 |
| per_page | int | 每页数量 |
| status | string | 订单状态 |

**订单状态**:
- pending: 待支付
- paid: 已支付
- shipped: 已发货
- completed: 已完成
- cancelled: 已取消
- refunded: 已退款

---

### 4.2 获取订单详情

**GET** `/orders/<order_id>`

**需要认证**: 是

**响应**:
```json
{
    "code": 200,
    "message": "操作成功",
    "data": {
        "id": 1,
        "order_no": "ORD20240101120000ABC123",
        "user_id": 1,
        "total_amount": 6999.00,
        "status": "pending",
        "payment_method": null,
        "shipping_address": "北京市朝阳区xxx",
        "created_at": "2024-01-01T12:00:00",
        "items": [
            {
                "id": 1,
                "product_id": 1,
                "product_name": "iPhone 15",
                "price": 6999.00,
                "quantity": 1,
                "subtotal": 6999.00
            }
        ]
    }
}
```

---

### 4.3 创建订单

**POST** `/orders`

**需要认证**: 是

**请求体**:
```json
{
    "shipping_address": "北京市朝阳区xxx街道xxx号"
}
```

---

### 4.4 支付订单

**POST** `/orders/<order_id>/pay`

**需要认证**: 是

**请求体**:
```json
{
    "payment_method": "alipay"  // alipay, wechat, card
}
```

---

### 4.5 取消订单

**POST** `/orders/<order_id>/cancel`

**需要认证**: 是

---

### 4.6 申请退款

**POST** `/orders/<order_id>/refund`

**需要认证**: 是

---

## 5. 文件管理模块

### 5.1 获取文件列表

**GET** `/files`

**需要认证**: 是

**查询参数**:
| 参数 | 类型 | 说明 |
|------|------|------|
| page | int | 页码 |
| per_page | int | 每页数量 |
| file_type | string | 文件类型(png/jpg/pdf等) |

---

### 5.2 上传文件

**POST** `/files/upload`

**需要认证**: 是

**Content-Type**: multipart/form-data

**表单字段**:
| 字段 | 类型 | 说明 |
|------|------|------|
| file | file | 文件 |

**支持的文件类型**: png, jpg, jpeg, gif, pdf, doc, docx, txt

**最大文件大小**: 16MB

---

### 5.3 获取文件信息

**GET** `/files/<file_id>`

**需要认证**: 是

---

### 5.4 下载文件

**GET** `/files/<file_id>/download`

**需要认证**: 是

---

### 5.5 删除文件

**DELETE** `/files/<file_id>`

**需要认证**: 是

---

## 6. 数据查询模块

### 6.1 高级商品查询

**GET** `/query/products`

**需要认证**: 否

**查询参数**:
| 参数 | 类型 | 说明 |
|------|------|------|
| page | int | 页码 |
| per_page | int | 每页数量 |
| category_id | int | 分类ID |
| keyword | string | 关键词(搜索名称和描述) |
| min_price | float | 最低价格 |
| max_price | float | 最高价格 |
| in_stock | string | 是否有库存(true/false) |
| sort_by | string | 排序字段 |
| sort_order | string | 排序方式 |

---

### 6.2 获取统计数据（管理员）

**GET** `/query/stats`

**需要认证**: 是（管理员）

**响应**:
```json
{
    "code": 200,
    "message": "操作成功",
    "data": {
        "users": {"total": 100, "active": 95},
        "products": {"total": 50, "active": 45, "out_of_stock": 5},
        "orders": {
            "total": 200,
            "by_status": {
                "pending": {"count": 10, "amount": 5000},
                "paid": {"count": 50, "amount": 25000}
            }
        },
        "revenue": 100000.00,
        "categories": [
            {"name": "电子产品", "product_count": 20}
        ]
    }
}
```

---

### 6.3 订单聚合查询（管理员）

**GET** `/query/orders/aggregate`

**需要认证**: 是（管理员）

**查询参数**:
| 参数 | 类型 | 说明 |
|------|------|------|
| group_by | string | 分组方式(day/month/status) |

---

### 6.4 热销商品排行（管理员）

**GET** `/query/products/top`

**需要认证**: 是（管理员）

**查询参数**:
| 参数 | 类型 | 说明 |
|------|------|------|
| limit | int | 返回数量，默认10 |

---

## 7. 管理员接口

### 7.1 获取用户列表

**GET** `/admin/users`

**需要认证**: 是（管理员）

---

### 7.2 获取用户详情

**GET** `/admin/users/<user_id>`

**需要认证**: 是（管理员）

---

### 7.3 更新用户

**PUT** `/admin/users/<user_id>`

**需要认证**: 是（管理员）

**请求体**:
```json
{
    "role": "admin",  // admin, user
    "is_active": true
}
```

---

### 7.4 删除用户

**DELETE** `/admin/users/<user_id>`

**需要认证**: 是（管理员）

---

### 7.5 获取所有订单

**GET** `/admin/orders`

**需要认证**: 是（管理员）

**查询参数**:
| 参数 | 类型 | 说明 |
|------|------|------|
| page | int | 页码 |
| per_page | int | 每页数量 |
| status | string | 订单状态 |
| user_id | int | 用户ID |

---

### 7.6 更新订单状态

**PUT** `/admin/orders/<order_id>/status`

**需要认证**: 是（管理员）

**请求体**:
```json
{
    "status": "shipped"
}
```

---

## 错误码说明

| 错误码 | 说明 |
|--------|------|
| 200 | 成功 |
| 201 | 创建成功 |
| 400 | 请求参数错误 |
| 401 | 未认证/Token无效 |
| 403 | 权限不足 |
| 404 | 资源不存在 |
| 500 | 服务器内部错误 |

---

## 测试账号

| 角色 | 用户名 | 密码 |
|------|--------|------|
| 管理员 | admin | admin123 |
| 普通用户 | testuser | test123 |
