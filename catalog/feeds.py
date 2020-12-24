from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Product


class LatestProductsFeed(Feed):
    title = 'Products'
    link = '/product/'
    description = 'Recent items'

    def items(self):
        return Product.objects.all().order_by('-created')[:15]

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return truncatewords(item.description, 30)
