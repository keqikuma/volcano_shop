from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_product, name='upload_product'),
    path('', views.store, name='store'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),

    # 后面会添加其他视图（首页、详情页等）
]
