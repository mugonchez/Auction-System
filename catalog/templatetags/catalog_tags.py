from django import template
from catalog.models import Product
from orders.models import Order
from django.db.models import Count
register = template.Library()


@register.inclusion_tag('catalog/latest_items.html')
def show_latest_items(count=5):
    latest_items = Product.objects.order_by('-created')[:count]
    return {'latest_items': latest_items}


@register.inclusion_tag('catalog/most_reviewed.html')
def get_most_reviewed_items(count=3):
    most_reviewed = Product.objects.annotate(total_reviews=Count('reviews')).order_by('-total_reviews')[:count]
    return {'most_reviewed': most_reviewed}


@register.inclusion_tag('catalog/most_purchased.html')
def get_most_purchased_items(count=3):
    most_purchased = Order.objects.order_by('-quantity')[:count]
    return {'most_purchased': most_purchased}









