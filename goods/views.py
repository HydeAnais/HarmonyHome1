from django.shortcuts import render
from goods.templatetags import custom_tags

def catalog(request):
    return render(request, 'goods/catalog.html')


def product(request):
    return render(request, 'goods/product.html')