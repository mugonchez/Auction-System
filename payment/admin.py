from django.contrib import admin
from .models import Payment, Balance


class AdminPayment(admin.ModelAdmin):
    list_display = ['code', 'active', 'created', 'user']
    search_fields = ['code']
admin.site.register(Payment, AdminPayment)


class AdminBalance(admin.ModelAdmin):
    list_display = ['user', 'credit_number', 'amount', 'created']
admin.site.register(Balance, AdminBalance)

