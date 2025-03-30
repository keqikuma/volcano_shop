from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProductForm

@login_required
def upload_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user  # 当前登录用户为卖家
            product.save()
            return redirect('store')  # 上传成功后跳转到首页（可改为商品详情页）
    else:
        form = ProductForm()
    return render(request, 'upload_product.html', {'form': form})
