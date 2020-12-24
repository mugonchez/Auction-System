from catalog.models import Product
from django.shortcuts import get_object_or_404
from cart.cart import Cart


def get_stock(request, product_id):
    cart = Cart(request)
    for item in cart:
        product = get_object_or_404(Product, id=product_id)
        sub = item['quantity']
        prod = item['product']
        stocks = prod.stock - sub
        product.stock = stocks
    product.save()
