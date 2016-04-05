from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from .recommender import Recommender
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    # price_filter_start = request.GET.get('price_filter_start', None)
    # price_filter_end = request.GET.get('price_filter_end', None)

    print(request.GET)
    
    category = None
    products = Product.objects.filter(available=True)
    new_products = Product.objects.order_by('pk')[:5]
    all_cat = True
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        all_cat = False
    return render(request,
                  'shop/product/list.html',
                  {'all_cat': all_cat,
                   'category': category,
                   'products': products,
                   'new_products': new_products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)

    products = Product.objects.filter(available=True)
    category_products = products.filter(category=product.category)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'recommended_products': recommended_products,
                   'category_products': category_products})
