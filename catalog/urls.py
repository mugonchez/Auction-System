from django.urls import re_path
from . import views
from .feeds import LatestProductsFeed

app_name = 'catalog'


urlpatterns = [
    re_path(r'^$', views.product_list, name='product_list'),
    re_path(r'^feed/$', LatestProductsFeed(), name='product_feed'),
    re_path(r'^help/$', views.help_center, name='help'),
    re_path(r'^careers/$', views.careers, name='careers'),
    re_path(r'^conditions/$', views.conditions, name='conditions'),
    re_path(r'^contact/us/$', views.contact, name='contact'),
    re_path(r'^delivery/$', views.delivery, name='delivery'),
    re_path(r'^secure/payment/$', views.secure_payment, name='payment'),
    re_path(r'^privacy/policy/$', views.privacy, name='privacy'),
    re_path(r'^responsibility/$', views.responsibility, name='responsibility'),
    re_path(r'^returns/$', views.returns_policy, name='returns'),
    re_path(r'^feedback/$', views.feedback, name='feedback'),
    re_path(r'^(?P<id>\d+)/$', views.product_review, name='product_review'),
    re_path(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    re_path(r'^bid/(?P<id>\d+)/$', views.bid_detail, name='bid_detail'),

]
