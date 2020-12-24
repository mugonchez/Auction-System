from django.urls import re_path
from . import views


app_name = 'account'


urlpatterns = [
    re_path(r'^$', views.dashboard, name='dashboard'),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^edit/$', views.edit, name='edit'),
    re_path(r'^cancel/(?P<order_id>\d+)/$', views.cancel_order, name='cancel_order'),
    re_path(r'^clear/(?P<order_id>\d+)/$', views.clear_order, name='clear_order'),
    re_path(r'^pay/bid/(?P<id>\d+)/$', views.pay_bid, name='pay_bid'),
]
