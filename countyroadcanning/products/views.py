from django.shortcuts import render
from .models import Product


# Create your views here.
def products(request):
    items = Product.objects.all()
    return render(request, 'products/products.html', {"products": items})

def product(request, prod_id):
    item = Product.objects.get(id = prod_id)
    item.price = (item.price / 100)
    return render(request, 'products/product_page.html', {'product': item})
