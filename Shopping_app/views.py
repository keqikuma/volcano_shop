from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from django.core.paginator import Paginator
from .models import Product
from django.db.models import Q

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

def store(request):
    query = request.GET.get('query')
    products = Product.objects.filter(is_sold=False)

    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(brand__icontains=query) |
            Q(category__icontains=query) |
            Q(tags__icontains=query)
        )

    paginator = Paginator(products.order_by('-created_at'), 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'store/store.html', {
        'page_obj': page_obj,
        'query': query  # 👉 传回前端保留输入框值
    })

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'store/product_detail.html', {'product': product})