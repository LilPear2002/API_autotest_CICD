# Flask商城 元素定位文档

本文档提供Web自动化测试所需的页面元素定位信息，适用于Selenium/Playwright等自动化测试框架。

---

## 1. 公共导航栏

| 元素 | ID | CSS选择器 | 说明 |
|------|-----|-----------|------|
| 导航栏 | main-nav | nav.navbar | 顶部导航栏 |
| Logo | nav-brand | .navbar-brand | 网站Logo |
| 首页链接 | nav-home | #nav-home | 首页导航 |
| 商品链接 | nav-products | #nav-products | 商品页导航 |
| 搜索框 | search-input | #search-input | 搜索输入框 |
| 搜索按钮 | search-btn | #search-btn | 搜索按钮 |
| 购物车 | nav-cart | #nav-cart | 购物车链接 |
| 用户下拉菜单 | userDropdown | #userDropdown | 用户菜单 |
| 登录链接 | nav-login | #nav-login | 登录链接 |
| 注册链接 | nav-register | #nav-register | 注册链接 |

### 用户下拉菜单项

| 元素 | ID | 说明 |
|------|-----|------|
| 个人中心 | menu-profile | 个人中心链接 |
| 我的订单 | menu-orders | 订单列表链接 |
| 文件管理 | menu-files | 文件管理链接 |
| 管理后台 | menu-admin | 管理后台链接(管理员) |
| 退出登录 | menu-logout | 登出链接 |

---

## 2. 首页 (/)

| 元素 | ID | 说明 |
|------|-----|------|
| Hero区域 | hero-section | 首页横幅区域 |
| Hero标题 | hero-title | 欢迎标题 |
| Hero描述 | hero-desc | 描述文字 |
| 浏览商品按钮 | hero-btn | 跳转商品页按钮 |
| 分类区域 | categories-section | 分类展示区 |
| 分类标题 | categories-title | 分类标题 |
| 分类按钮 | category-{id} | 各分类按钮 |
| 商品区域 | products-section | 商品展示区 |
| 商品标题 | products-title | 最新商品标题 |
| 商品卡片 | product-card-{id} | 商品卡片 |
| 商品图片 | product-img-{id} | 商品图片 |
| 商品名称 | product-name-{id} | 商品名称 |
| 商品价格 | product-price-{id} | 商品价格 |
| 商品库存 | product-stock-{id} | 库存信息 |
| 查看详情按钮 | product-detail-btn-{id} | 详情按钮 |
| 无商品提示 | no-products | 暂无商品提示 |

---

## 3. 登录页 (/login)

| 元素 | ID | CSS选择器 | 说明 |
|------|-----|-----------|------|
| 登录卡片 | login-card | #login-card | 登录表单容器 |
| 登录标题 | login-title | #login-title | 页面标题 |
| 登录表单 | login-form | #login-form | 表单元素 |
| 用户名输入框 | username | input#username | 用户名输入 |
| 密码输入框 | password | input#password | 密码输入 |
| 登录按钮 | login-btn | #login-btn | 提交按钮 |
| 注册链接 | register-link | #register-link a | 跳转注册 |

---

## 4. 注册页 (/register)

| 元素 | ID | CSS选择器 | 说明 |
|------|-----|-----------|------|
| 注册卡片 | register-card | #register-card | 注册表单容器 |
| 注册标题 | register-title | #register-title | 页面标题 |
| 注册表单 | register-form | #register-form | 表单元素 |
| 用户名输入框 | username | input#username | 用户名输入 |
| 邮箱输入框 | email | input#email | 邮箱输入 |
| 密码输入框 | password | input#password | 密码输入 |
| 确认密码输入框 | confirm_password | input#confirm_password | 确认密码 |
| 注册按钮 | register-btn | #register-btn | 提交按钮 |
| 登录链接 | login-link | #login-link a | 跳转登录 |

---

## 5. 商品列表页 (/products)

| 元素 | ID | 说明 |
|------|-----|------|
| 侧边栏 | sidebar | 筛选侧边栏 |
| 筛选标题 | filter-header | 筛选区标题 |
| 分类筛选 | category-filter | 分类筛选列表 |
| 全部分类 | category-all | 全部分类选项 |
| 分类选项 | category-filter-{id} | 各分类选项 |
| 商品列表 | product-list | 商品列表区域 |
| 搜索结果提示 | search-result | 搜索结果信息 |
| 商品卡片 | product-card-{id} | 商品卡片 |
| 商品图片 | product-img-{id} | 商品图片 |
| 商品名称 | product-name-{id} | 商品名称 |
| 商品价格 | product-price-{id} | 商品价格 |
| 商品库存 | product-stock-{id} | 库存信息 |
| 详情按钮 | product-detail-btn-{id} | 查看详情 |
| 无商品提示 | no-products | 暂无商品 |
| 分页 | pagination | 分页导航 |
| 上一页 | page-prev | 上一页按钮 |
| 下一页 | page-next | 下一页按钮 |
| 页码 | page-{n} | 页码按钮 |

---

## 6. 商品详情页 (/products/{id})

| 元素 | ID | 说明 |
|------|-----|------|
| 面包屑 | breadcrumb | 面包屑导航 |
| 商品详情区 | product-detail | 详情区域 |
| 商品图片 | product-image | 商品大图 |
| 商品名称 | product-name | 商品名称 |
| 商品分类 | product-category | 所属分类 |
| 商品价格 | product-price | 商品价格 |
| 库存状态 | product-stock | 库存信息 |
| 商品描述 | product-description | 描述区域 |
| 加入购物车表单 | add-to-cart-form | 购物车表单 |
| 数量减少 | quantity-minus | 减少数量按钮 |
| 数量输入 | quantity | 数量输入框 |
| 数量增加 | quantity-plus | 增加数量按钮 |
| 加入购物车 | add-to-cart-btn | 加入购物车按钮 |
| 登录购买 | login-to-buy | 登录后购买按钮 |

---

## 7. 购物车页 (/cart)

| 元素 | ID | 说明 |
|------|-----|------|
| 购物车标题 | cart-title | 页面标题 |
| 购物车表格容器 | cart-table-container | 表格容器 |
| 购物车表格 | cart-table | 购物车表格 |
| 购物车项列表 | cart-items | 商品列表tbody |
| 购物车项 | cart-item-{id} | 单个商品行 |
| 商品链接 | cart-product-link-{id} | 商品名称链接 |
| 商品单价 | cart-item-price-{id} | 单价显示 |
| 减少数量 | cart-minus-{id} | 减少按钮 |
| 数量显示 | cart-quantity-{id} | 数量输入框 |
| 增加数量 | cart-plus-{id} | 增加按钮 |
| 小计 | cart-subtotal-{id} | 小计金额 |
| 删除按钮 | cart-remove-{id} | 删除商品 |
| 总计 | cart-total | 总金额 |
| 购物车操作 | cart-actions | 操作按钮区 |
| 清空购物车 | clear-cart-btn | 清空按钮 |
| 去结算 | checkout-btn | 结算按钮 |
| 空购物车 | empty-cart | 空购物车提示 |
| 去购物按钮 | go-shopping-btn | 去购物按钮 |

### 结算弹窗

| 元素 | ID | 说明 |
|------|-----|------|
| 弹窗标题 | checkout-modal-title | 弹窗标题 |
| 收货地址 | shipping_address | 地址输入框 |
| 订单金额 | checkout-total | 金额显示 |
| 取消按钮 | checkout-cancel | 取消按钮 |
| 提交订单 | confirm-checkout-btn | 提交按钮 |

---

## 8. 订单列表页 (/orders)

| 元素 | ID | 说明 |
|------|-----|------|
| 订单标题 | orders-title | 页面标题 |
| 订单表格容器 | orders-table-container | 表格容器 |
| 订单表格 | orders-table | 订单表格 |
| 订单列表 | orders-list | 订单tbody |
| 订单行 | order-row-{id} | 单个订单行 |
| 订单号 | order-no-{id} | 订单号 |
| 订单金额 | order-amount-{id} | 订单金额 |
| 订单状态 | order-status-{id} | 订单状态 |
| 创建时间 | order-time-{id} | 创建时间 |
| 详情按钮 | order-detail-btn-{id} | 查看详情 |
| 无订单提示 | no-orders | 暂无订单 |
| 去购物按钮 | go-shopping-btn | 去购物按钮 |
| 分页 | pagination | 分页导航 |


---

## 9. 订单详情页 (/orders/{id})

| 元素 | ID | 说明 |
|------|-----|------|
| 面包屑 | breadcrumb | 面包屑导航 |
| 订单信息卡片 | order-info-card | 订单信息区 |
| 订单号 | order-no | 订单号显示 |
| 订单状态 | order-status | 状态徽章 |
| 创建时间 | order-created-at | 创建时间 |
| 收货地址 | order-address | 收货地址 |
| 支付方式 | order-payment | 支付方式 |
| 订单金额 | order-amount | 订单金额 |
| 商品列表卡片 | order-items-card | 商品列表区 |
| 商品表格 | order-items-table | 商品表格 |
| 商品列表 | order-items | 商品tbody |
| 商品项 | order-item-{id} | 单个商品行 |
| 商品名称 | item-name-{id} | 商品名称 |
| 商品单价 | item-price-{id} | 商品单价 |
| 商品数量 | item-quantity-{id} | 商品数量 |
| 商品小计 | item-subtotal-{id} | 小计金额 |
| 操作区 | order-actions | 操作按钮区 |
| 支付按钮 | pay-btn | 立即支付 |
| 取消按钮 | cancel-btn | 取消订单 |
| 退款按钮 | refund-btn | 申请退款 |

### 支付弹窗

| 元素 | ID | 说明 |
|------|-----|------|
| 弹窗标题 | pay-modal-title | 弹窗标题 |
| 支付宝选项 | pay-alipay | 支付宝单选 |
| 微信选项 | pay-wechat | 微信单选 |
| 银行卡选项 | pay-card | 银行卡单选 |
| 取消按钮 | pay-cancel | 取消按钮 |
| 确认支付 | confirm-pay-btn | 确认支付按钮 |

---

## 10. 个人中心页 (/profile)

| 元素 | ID | 说明 |
|------|-----|------|
| 头像卡片 | profile-card | 头像信息卡片 |
| 用户名 | profile-username | 用户名显示 |
| 角色 | profile-role | 角色徽章 |
| 信息卡片 | info-card | 基本信息卡片 |
| 信息表单 | profile-form | 信息表单 |
| 用户名输入 | info-username | 用户名(禁用) |
| 邮箱输入 | info-email | 邮箱输入框 |
| 注册时间 | info-created | 注册时间(禁用) |
| 保存按钮 | update-profile-btn | 保存修改按钮 |
| 密码卡片 | password-card | 修改密码卡片 |
| 密码表单 | password-form | 密码表单 |
| 旧密码 | old_password | 旧密码输入 |
| 新密码 | new_password | 新密码输入 |
| 确认密码 | confirm_password | 确认密码输入 |
| 修改密码按钮 | change-password-btn | 修改密码按钮 |

---

## 11. 文件管理页 (/files)

| 元素 | ID | 说明 |
|------|-----|------|
| 文件标题 | files-title | 页面标题 |
| 上传按钮 | upload-btn | 上传文件按钮 |
| 文件表格容器 | files-table-container | 表格容器 |
| 文件表格 | files-table | 文件表格 |
| 文件列表 | files-list | 文件tbody |
| 文件行 | file-row-{id} | 单个文件行 |
| 文件名 | file-name-{id} | 文件名 |
| 文件类型 | file-type-{id} | 文件类型 |
| 文件大小 | file-size-{id} | 文件大小 |
| 上传时间 | file-time-{id} | 上传时间 |
| 下载按钮 | file-download-{id} | 下载按钮 |
| 删除按钮 | file-delete-{id} | 删除按钮 |
| 无文件提示 | no-files | 暂无文件 |
| 分页 | pagination | 分页导航 |

### 上传弹窗

| 元素 | ID | 说明 |
|------|-----|------|
| 弹窗标题 | upload-modal-title | 弹窗标题 |
| 上传表单 | upload-form | 上传表单 |
| 文件选择 | file | 文件输入框 |
| 取消按钮 | upload-cancel | 取消按钮 |
| 确认上传 | confirm-upload-btn | 上传按钮 |

---

## 12. 管理后台 - 首页 (/admin)

| 元素 | ID | 说明 |
|------|-----|------|
| 管理标题 | admin-title | 页面标题 |
| 统计卡片区 | stats-cards | 统计卡片区域 |
| 用户统计卡片 | stat-users | 用户数卡片 |
| 用户数量 | stat-users-count | 用户数量 |
| 用户详情链接 | stat-users-link | 查看详情 |
| 商品统计卡片 | stat-products | 商品数卡片 |
| 商品数量 | stat-products-count | 商品数量 |
| 商品详情链接 | stat-products-link | 查看详情 |
| 订单统计卡片 | stat-orders | 订单数卡片 |
| 订单数量 | stat-orders-count | 订单数量 |
| 订单详情链接 | stat-orders-link | 查看详情 |
| 分类统计卡片 | stat-categories | 分类数卡片 |
| 分类数量 | stat-categories-count | 分类数量 |
| 分类详情链接 | stat-categories-link | 查看详情 |
| 最近订单卡片 | recent-orders-card | 最近订单区 |
| 最近订单表格 | recent-orders-table | 订单表格 |
| 最近订单列表 | recent-orders-list | 订单tbody |
| 最近订单项 | recent-order-{id} | 单个订单 |
| 快捷操作卡片 | quick-links-card | 快捷操作区 |
| 快捷操作列表 | quick-links | 操作按钮列表 |
| 添加商品 | quick-add-product | 添加商品按钮 |
| 管理分类 | quick-add-category | 管理分类按钮 |
| 用户管理 | quick-manage-users | 用户管理按钮 |
| 订单管理 | quick-manage-orders | 订单管理按钮 |

---

## 13. 管理后台 - 用户管理 (/admin/users)

| 元素 | ID | 说明 |
|------|-----|------|
| 面包屑 | breadcrumb | 面包屑导航 |
| 用户标题 | users-title | 页面标题 |
| 用户表格容器 | users-table-container | 表格容器 |
| 用户表格 | users-table | 用户表格 |
| 用户列表 | users-list | 用户tbody |
| 用户行 | user-row-{id} | 单个用户行 |
| 用户ID | user-id-{id} | 用户ID |
| 用户名 | user-name-{id} | 用户名 |
| 用户邮箱 | user-email-{id} | 邮箱 |
| 角色选择 | user-role-{id} | 角色下拉框 |
| 状态开关 | user-active-{id} | 状态开关 |
| 注册时间 | user-created-{id} | 注册时间 |
| 删除按钮 | user-delete-{id} | 删除按钮 |
| 分页 | pagination | 分页导航 |

---

## 14. 管理后台 - 商品管理 (/admin/products)

| 元素 | ID | 说明 |
|------|-----|------|
| 面包屑 | breadcrumb | 面包屑导航 |
| 商品标题 | products-title | 页面标题 |
| 添加商品按钮 | add-product-btn | 添加商品 |
| 商品表格容器 | products-table-container | 表格容器 |
| 商品表格 | products-table | 商品表格 |
| 商品列表 | products-list | 商品tbody |
| 商品行 | product-row-{id} | 单个商品行 |
| 商品ID | product-id-{id} | 商品ID |
| 商品名称 | product-name-{id} | 商品名称 |
| 商品分类 | product-category-{id} | 所属分类 |
| 商品价格 | product-price-{id} | 商品价格 |
| 商品库存 | product-stock-{id} | 库存数量 |
| 商品状态 | product-status-{id} | 上架状态 |
| 编辑按钮 | product-edit-{id} | 编辑按钮 |
| 删除按钮 | product-delete-{id} | 删除按钮 |
| 分页 | pagination | 分页导航 |

### 商品弹窗

| 元素 | ID | 说明 |
|------|-----|------|
| 弹窗标题 | product-modal-title | 弹窗标题 |
| 商品表单 | product-form | 商品表单 |
| 商品ID | product-id | 隐藏ID |
| 商品名称输入 | product-name-input | 名称输入 |
| 商品描述输入 | product-description-input | 描述输入 |
| 商品价格输入 | product-price-input | 价格输入 |
| 商品库存输入 | product-stock-input | 库存输入 |
| 分类选择 | product-category-input | 分类下拉 |
| 上架开关 | product-active-input | 上架开关 |
| 取消按钮 | product-cancel | 取消按钮 |
| 保存按钮 | save-product-btn | 保存按钮 |

---

## 15. 管理后台 - 订单管理 (/admin/orders)

| 元素 | ID | 说明 |
|------|-----|------|
| 面包屑 | breadcrumb | 面包屑导航 |
| 订单标题 | orders-title | 页面标题 |
| 状态筛选 | status-filter | 状态筛选区 |
| 全部筛选 | filter-all | 全部按钮 |
| 待支付筛选 | filter-pending | 待支付按钮 |
| 已支付筛选 | filter-paid | 已支付按钮 |
| 已发货筛选 | filter-shipped | 已发货按钮 |
| 已完成筛选 | filter-completed | 已完成按钮 |
| 已取消筛选 | filter-cancelled | 已取消按钮 |
| 已退款筛选 | filter-refunded | 已退款按钮 |
| 订单表格容器 | orders-table-container | 表格容器 |
| 订单表格 | orders-table | 订单表格 |
| 订单列表 | orders-list | 订单tbody |
| 订单行 | order-row-{id} | 单个订单行 |
| 订单号 | order-no-{id} | 订单号 |
| 用户ID | order-user-{id} | 用户ID |
| 订单金额 | order-amount-{id} | 订单金额 |
| 状态选择 | order-status-{id} | 状态下拉框 |
| 创建时间 | order-time-{id} | 创建时间 |
| 详情按钮 | order-view-{id} | 查看详情 |
| 分页 | pagination | 分页导航 |

---

## 16. 管理后台 - 分类管理 (/admin/categories)

| 元素 | ID | 说明 |
|------|-----|------|
| 面包屑 | breadcrumb | 面包屑导航 |
| 分类标题 | categories-title | 页面标题 |
| 添加分类按钮 | add-category-btn | 添加分类 |
| 分类表格容器 | categories-table-container | 表格容器 |
| 分类表格 | categories-table | 分类表格 |
| 分类列表 | categories-list | 分类tbody |
| 分类行 | category-row-{id} | 单个分类行 |
| 分类ID | category-id-{id} | 分类ID |
| 分类名称 | category-name-{id} | 分类名称 |
| 分类描述 | category-desc-{id} | 分类描述 |
| 商品数量 | category-count-{id} | 商品数量 |
| 编辑按钮 | category-edit-{id} | 编辑按钮 |
| 删除按钮 | category-delete-{id} | 删除按钮 |
| 无分类提示 | no-categories | 暂无分类 |

### 分类弹窗

| 元素 | ID | 说明 |
|------|-----|------|
| 弹窗标题 | category-modal-title | 弹窗标题 |
| 分类表单 | category-form | 分类表单 |
| 分类ID | category-id-input | 隐藏ID |
| 分类名称输入 | category-name-input | 名称输入 |
| 分类描述输入 | category-description-input | 描述输入 |
| 取消按钮 | category-cancel | 取消按钮 |
| 保存按钮 | save-category-btn | 保存按钮 |

---

## 定位策略建议

### 优先级

1. **ID定位** - 最稳定，推荐首选
2. **CSS选择器** - 灵活性高
3. **XPath** - 复杂场景使用

### 示例代码 (Python + Selenium)

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# ID定位
login_btn = driver.find_element(By.ID, "login-btn")

# CSS选择器
username_input = driver.find_element(By.CSS_SELECTOR, "#username")

# 动态ID定位
product_card = driver.find_element(By.ID, f"product-card-{product_id}")

# 组合定位
cart_item = driver.find_element(By.CSS_SELECTOR, f"#cart-item-{item_id} .quantity-btn")
```

### 示例代码 (Python + Playwright)

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    # ID定位
    page.click("#login-btn")
    
    # 填写表单
    page.fill("#username", "testuser")
    page.fill("#password", "123456")
    
    # 动态元素
    page.click(f"#product-detail-btn-{product_id}")
```

---

## 注意事项

1. 动态ID中的 `{id}` 需要替换为实际的数据库ID
2. 部分元素仅在特定条件下显示（如登录后才显示购物车）
3. 弹窗元素需要等待弹窗显示后才能操作
4. 分页元素的页码是动态生成的


---

## 常见测试场景操作步骤

### 场景1：用户注册

```
1. 打开首页 → 点击 #nav-register
2. 填写 #username → 输入用户名
3. 填写 #email → 输入邮箱
4. 填写 #password → 输入密码
5. 填写 #confirm_password → 确认密码
6. 点击 #register-btn → 提交注册
7. 验证跳转到登录页 → 检查 #login-title 存在
```

### 场景2：用户登录

```
1. 打开首页 → 点击 #nav-login
2. 填写 #username → 输入用户名
3. 填写 #password → 输入密码
4. 点击 #login-btn → 提交登录
5. 验证登录成功 → 检查 #userDropdown 显示用户名
```

### 场景3：用户登出

```
1. 点击 #userDropdown → 展开用户菜单
2. 点击 #menu-logout → 退出登录
3. 验证登出成功 → 检查 #nav-login 存在
```

### 场景4：修改个人信息

```
1. 点击 #userDropdown → 展开用户菜单
2. 点击 #menu-profile → 进入个人中心
3. 修改 #info-email → 输入新邮箱
4. 点击 #update-profile-btn → 保存修改
5. 验证弹窗提示 → 检查alert内容
```

### 场景5：修改密码

```
1. 进入个人中心页面
2. 填写 #old_password → 输入旧密码
3. 填写 #new_password → 输入新密码
4. 填写 #confirm_password → 确认新密码
5. 点击 #change-password-btn → 提交修改
6. 验证弹窗提示 → 检查alert内容
```

### 场景6：搜索商品

```
1. 在导航栏找到 #search-input → 输入关键词
2. 点击 #search-btn → 执行搜索
3. 验证搜索结果 → 检查 #search-result 显示结果数量
4. 验证商品列表 → 检查 #product-list 中的商品卡片
```

### 场景7：按分类筛选商品

```
1. 打开商品列表页 /products
2. 在侧边栏 #category-filter 中点击目标分类
3. 验证URL参数 → 检查 category_id 参数
4. 验证商品列表 → 检查显示的商品属于该分类
```

### 场景8：查看商品详情

```
1. 在商品列表中找到目标商品卡片 #product-card-{id}
2. 点击 #product-detail-btn-{id} → 进入详情页
3. 验证商品信息 → 检查 #product-name, #product-price, #product-stock
```

### 场景9：添加商品到购物车

```
1. 进入商品详情页
2. 调整数量 → 点击 #quantity-plus 或 #quantity-minus
3. 或直接修改 #quantity 输入框的值
4. 点击 #add-to-cart-btn → 添加到购物车
5. 验证弹窗提示 → 检查alert显示"添加成功"
```

### 场景10：修改购物车商品数量

```
1. 点击 #nav-cart → 进入购物车页面
2. 找到目标商品行 #cart-item-{id}
3. 点击 #cart-plus-{id} 增加数量 或 #cart-minus-{id} 减少数量
4. 验证页面刷新 → 检查 #cart-quantity-{id} 和 #cart-total 更新
```

### 场景11：删除购物车商品

```
1. 进入购物车页面
2. 找到目标商品行 #cart-item-{id}
3. 点击 #cart-remove-{id} → 删除商品
4. 确认弹窗 → 点击确定
5. 验证商品已删除 → 检查 #cart-item-{id} 不存在
```

### 场景12：清空购物车

```
1. 进入购物车页面
2. 点击 #clear-cart-btn → 清空购物车
3. 确认弹窗 → 点击确定
4. 验证购物车为空 → 检查 #empty-cart 显示
```

### 场景13：创建订单（完整购物流程）

```
1. 登录账号
2. 浏览商品 → 点击 #nav-products
3. 选择商品 → 点击 #product-detail-btn-{id}
4. 添加购物车 → 点击 #add-to-cart-btn
5. 进入购物车 → 点击 #nav-cart
6. 点击结算 → 点击 #checkout-btn
7. 填写地址 → 在 #shipping_address 输入收货地址
8. 提交订单 → 点击 #confirm-checkout-btn
9. 验证跳转 → 检查进入订单详情页
```

### 场景14：支付订单

```
1. 进入订单详情页 /orders/{id}
2. 确认订单状态为待支付 → 检查 #order-status 显示"待支付"
3. 点击 #pay-btn → 打开支付弹窗
4. 选择支付方式 → 点击 #pay-alipay / #pay-wechat / #pay-card
5. 点击 #confirm-pay-btn → 确认支付
6. 验证支付成功 → 检查 #order-status 变为"已支付"
```

### 场景15：取消订单

```
1. 进入待支付订单详情页
2. 点击 #cancel-btn → 取消订单
3. 确认弹窗 → 点击确定
4. 验证取消成功 → 检查 #order-status 变为"已取消"
```

### 场景16：申请退款

```
1. 进入已支付订单详情页
2. 点击 #refund-btn → 申请退款
3. 确认弹窗 → 点击确定
4. 验证退款成功 → 检查 #order-status 变为"已退款"
```

### 场景17：上传文件

```
1. 点击 #userDropdown → 展开用户菜单
2. 点击 #menu-files → 进入文件管理
3. 点击 #upload-btn → 打开上传弹窗
4. 点击 #file → 选择文件
5. 点击 #confirm-upload-btn → 上传文件
6. 验证上传成功 → 检查文件列表中出现新文件
```

### 场景18：下载文件

```
1. 进入文件管理页面
2. 找到目标文件行 #file-row-{id}
3. 点击 #file-download-{id} → 下载文件
4. 验证文件下载 → 检查浏览器下载
```

### 场景19：删除文件

```
1. 进入文件管理页面
2. 找到目标文件行 #file-row-{id}
3. 点击 #file-delete-{id} → 删除文件
4. 确认弹窗 → 点击确定
5. 验证删除成功 → 检查 #file-row-{id} 不存在
```

### 场景20：管理员 - 添加商品

```
1. 使用管理员账号登录
2. 点击 #userDropdown → 展开用户菜单
3. 点击 #menu-admin → 进入管理后台
4. 点击 #stat-products-link 或 #quick-add-product → 进入商品管理
5. 点击 #add-product-btn → 打开添加弹窗
6. 填写 #product-name-input → 输入商品名称
7. 填写 #product-description-input → 输入描述
8. 填写 #product-price-input → 输入价格
9. 填写 #product-stock-input → 输入库存
10. 选择 #product-category-input → 选择分类
11. 勾选 #product-active-input → 设置上架
12. 点击 #save-product-btn → 保存商品
13. 验证添加成功 → 检查商品列表中出现新商品
```

### 场景21：管理员 - 编辑商品

```
1. 进入商品管理页面
2. 找到目标商品行 #product-row-{id}
3. 点击 #product-edit-{id} → 打开编辑弹窗
4. 修改相关字段
5. 点击 #save-product-btn → 保存修改
6. 验证修改成功 → 检查商品信息已更新
```

### 场景22：管理员 - 删除商品

```
1. 进入商品管理页面
2. 找到目标商品行 #product-row-{id}
3. 点击 #product-delete-{id} → 删除商品
4. 确认弹窗 → 点击确定
5. 验证删除成功 → 检查 #product-row-{id} 不存在
```

### 场景23：管理员 - 添加分类

```
1. 进入管理后台 → 点击 #quick-add-category
2. 点击 #add-category-btn → 打开添加弹窗
3. 填写 #category-name-input → 输入分类名称
4. 填写 #category-description-input → 输入描述
5. 点击 #save-category-btn → 保存分类
6. 验证添加成功 → 检查分类列表中出现新分类
```

### 场景24：管理员 - 修改用户角色

```
1. 进入管理后台 → 点击 #quick-manage-users
2. 找到目标用户行 #user-row-{id}
3. 在 #user-role-{id} 下拉框中选择新角色
4. 验证修改成功 → 检查角色已更新
```

### 场景25：管理员 - 禁用/启用用户

```
1. 进入用户管理页面
2. 找到目标用户行 #user-row-{id}
3. 点击 #user-active-{id} 开关 → 切换状态
4. 验证状态已更新
```

### 场景26：管理员 - 修改订单状态

```
1. 进入管理后台 → 点击 #quick-manage-orders
2. 可选：点击状态筛选按钮 #filter-pending 等
3. 找到目标订单行 #order-row-{id}
4. 在 #order-status-{id} 下拉框中选择新状态
5. 验证状态已更新
```

### 场景27：分页操作

```
1. 进入有分页的列表页面
2. 点击 #page-next → 下一页
3. 或点击 #page-prev → 上一页
4. 或点击 #page-{n} → 跳转到第n页
5. 验证页面数据已更新
```

---

## 等待策略建议

### 页面加载等待

```python
# Selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 等待元素可见
wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.ID, "login-btn")))

# 等待元素可点击
element = wait.until(EC.element_to_be_clickable((By.ID, "submit-btn")))
```

```python
# Playwright
# 自动等待，无需显式等待
page.click("#login-btn")

# 显式等待
page.wait_for_selector("#product-list")
page.wait_for_load_state("networkidle")
```

### 弹窗等待

```python
# Selenium - 等待Bootstrap Modal显示
wait.until(EC.visibility_of_element_located((By.ID, "productModal")))

# Playwright
page.wait_for_selector("#productModal.show")
```

### Alert处理

```python
# Selenium
from selenium.webdriver.common.alert import Alert
alert = Alert(driver)
alert_text = alert.text
alert.accept()  # 点击确定

# Playwright
page.on("dialog", lambda dialog: dialog.accept())
```

---

## 断言建议

### 常用断言点

| 场景 | 断言内容 | 元素/方式 |
|------|----------|-----------|
| 登录成功 | 用户名显示 | #userDropdown 文本 |
| 登录失败 | 错误提示 | alert 或 flash消息 |
| 注册成功 | 跳转登录页 | URL包含/login |
| 添加购物车 | 成功提示 | alert文本 |
| 购物车数量 | 数量正确 | #cart-quantity-{id} 值 |
| 订单创建 | 订单号生成 | #order-no 不为空 |
| 支付成功 | 状态变更 | #order-status 文本 |
| 商品搜索 | 结果数量 | #search-result 文本 |
| 分页 | 当前页码 | .page-item.active 文本 |
| 管理员权限 | 后台入口 | #menu-admin 存在 |

### 示例断言代码

```python
# Selenium
assert "登录成功" in driver.find_element(By.CLASS_NAME, "alert").text
assert driver.find_element(By.ID, "userDropdown").text == "testuser"
assert "pending" in driver.find_element(By.ID, "order-status").text

# Playwright
expect(page.locator("#userDropdown")).to_have_text("testuser")
expect(page.locator("#order-status")).to_contain_text("待支付")
expect(page).to_have_url(re.compile(r"/orders/\d+"))
```
