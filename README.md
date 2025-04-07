# SecondHand Shop - Django 二手商品平台

这是一个用 Django 构建的**简化版二手商品交易平台**，用户可以注册账号，自行上传商品信息（名称、价格、描述、图片），展示在商品广场上，未来支持订单、评论、收藏等扩展。

> 灵感来源于 eBay，但系统结构清晰、功能简洁，适合作为学习全栈开发、Django 模型设计、表单交互等内容的项目基础。


---

## 第一步：创建 Python 虚拟环境

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows 下使用 .venv\Scripts\activate
```
**目的**：  
使用虚拟环境隔离依赖，确保不会影响系统环境，并为每个项目创建独立的包管理空间。

## 第二步：安装 Django 框架

```bash
pip install django==4.1.2
pip install Pillow
pip freeze > requirements.txt
```


**目的**：  
安装 Django 并将版本固定，方便团队协作或服务器部署时保持一致性。
Django 是核心 Web 框架，Pillow 用于支持图片上传。

## 第三步：创建 Django 项目与应用
```bash
django-admin startproject mysite .
python manage.py startapp Shopping_app 
python manage.py startapp accounts
```


**目的**：

- `mysite/` 是主配置项目，包含全局 settings、urls、wsgi
    
- `Shopping_app/` 是商城核心应用（展示火山、购物车）
    
- `accounts/` 是用户账户系统（注册、登录）

## 第四步：注册 App 与配置静态资源

编辑 `mysite/settings.py`：

```python
INSTALLED_APPS = [
	...     
	'Shopping_app',
    'accounts', 
]  

STATIC_URL = 'static/'
STATICFILES_DIRS = [
	BASE_DIR / 'Shopping_app' / 'static',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

```

**目的**：

- 告诉 Django 我们创建了哪些应用
    
- 设置静态资源（CSS、图片、JS）加载路径
    

---

## 第五步：初始化数据库
```bash
python manage.py migrate
```


**目的**：  
将 Django 内置模型（如用户认证、会话）初始化到本地数据库（默认使用 SQLite）。

---

## 第六步：启动开发服务器

```bash
python manage.py runserver
```

**目的**：  
运行本地服务器，默认访问地址为 `http://127.0.0.1:8000`，用于本地开发与调试。

## 第 7 步：创建 `Product` 模型
```python
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    is_sold = models.BooleanField(default=False)
```

> 让用户可以上传商品，并自动记录时间和作者。

然后运行：
```bash
python manage.py makemigrations Shopping_app
python manage.py migrate
```

## 第八步：商品展示页、详情页与搜索功能实现

### 目标

实现一个电商平台的核心用户功能，包括：

- 商品首页展示（分页）
    
- 商品详情查看
    
- 搜索功能（支持关键词模糊搜索）
    

---

### 🛠 实现过程

#### 1️⃣ 商品首页展示（store 页面）

- 编写视图函数 `store()`，查询数据库中所有 `is_sold=False` 的商品。
    
- 使用 Django `Paginator` 实现分页，每页展示 12 个商品。
    
- 在模板 `store.html` 中渲染商品卡片，显示：
    
    - 商品名称、价格、品牌、成色、卖家
        
    - 支持图片展示，图片不存在时使用默认图。
        
- 商品卡片下方添加 “查看详情” 按钮，跳转到商品详情页。
    

#### 2️⃣ 商品详情页

- 编写视图函数 `product_detail(request, product_id)`，根据 ID 获取商品详情。
    
- 配置 URL 路由 `/product/<int:product_id>/`。
    
- 模板中展示商品所有字段信息，包括上传时间、描述、品牌、标签等。
    

#### 3️⃣ 搜索功能

- 在首页上方加入搜索框。
    
- 搜索支持关键词匹配商品 `名称 name`、`品牌 brand`、`标签 tags`、`类别 category`。
    
- 搜索结果使用原分页展示逻辑，不破坏首页结构。
    

---
## 尚未实现功能清单（核心功能&可选功能分级）

---

### 🧩 一、用户侧核心功能（电商必须有）❗

|功能|是否完成|描述|
|---|---|---|
|用户注册 / 登录 / 注销|❌|可使用 Django 内置 Auth 或自定义|
|我的商品管理页面|❌|用户查看 / 编辑 / 删除自己上传的商品|
|商品下架 / 删除|❌|卖家可以删除或标记商品已售出|
|收藏 / 点赞商品|❌|用户可以收藏喜欢的商品，形成“心愿单”|
|商品留言 / 评论|❌|商品详情页支持评论、回复（需评论模型）|

---

### 🎯 二、智能增强功能（用户体验提升）⭐

|功能|是否完成|描述|
|---|---|---|
|自动生成商品描述|❌|根据名称、品牌、类别生成一句商品介绍|
|智能价格建议|❌|结合类别、品牌、成色给出参考价格（AI / 数据分析）|
|商品标签推荐|❌|自动建议标签（如“数码”、“家具”）|
|图片识别补全字段|❌|上传图片后 AI 自动识别物品类型（可接入 API）|

---

### 🔐 三、权限与安全相关（进阶）🔐

|功能|是否完成|描述|
|---|---|---|
|上传权限校验|⚠️ 半成品|当前只有登录用户才能上传，但“我的商品”管理未限制操作权限|
|商品操作权限（仅卖家可编辑）|❌|商品编辑 / 删除权限控制|
|超级管理员后台审核|❌|上传商品需审核后上架（适合多用户平台）|

---

### 📦 四、运营辅助功能（上线平台需要）📈

|功能|是否完成|描述|
|---|---|---|
|商品分类筛选|❌|除搜索外支持按品牌、类别筛选|
|商品浏览量统计|❌|商品被查看次数记录（支持热门推荐）|
|站内消息通知|❌|系统向用户发送提示，如“您的商品已售出”等|
|支付接口 / 成交功能|❌|完善购物闭环（可模拟实现）|