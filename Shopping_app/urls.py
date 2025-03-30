from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_product, name='upload_product'),
    # 后面会添加其他视图（首页、详情页等）
]
