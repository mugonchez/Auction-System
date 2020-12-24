from django.contrib import admin
from .models import Category, Product, Review, Feedback, BidItems, Bidders


class AdminCategory(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, AdminCategory)


class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'available', 'created', 'modified',)
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ['modified']
admin.site.register(Product, AdminProduct)


class AdminReview(admin.ModelAdmin):
    list_display = ['user', 'created', 'modified', 'active' ]
    search_fields = ('body',)
    list_editable = ('active',)
    list_display_links = ['user']
admin.site.register(Review, AdminReview)


class AdminFeedback(admin.ModelAdmin):
    list_display = ['email', 'created', 'user', 'body']
    search_fields = ('email',)
admin.site.register(Feedback, AdminFeedback)


class AdminBidItems(admin.ModelAdmin):
    list_display = ('name', 'slug', 'minimum_price', 'available', 'created', 'modified','start_date', 'end_date')
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ['modified']
admin.site.register(BidItems, AdminBidItems)


class AdminBidders(admin.ModelAdmin):
    list_display = ('bidItem','won','phone_number', 'user', 'amount', 'active')
    search_fields = ('user',)
admin.site.register(Bidders, AdminBidders)




