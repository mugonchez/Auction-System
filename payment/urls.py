from django.urls import re_path
from . import views

app_name = 'payment'

urlpatterns = [
      re_path(r'^transact/$', views.payment_process, name='payment_process'),
      re_path(r'^top/up/$', views.credit_balance, name='credit_balance'),
      re_path(r'^activated/$', views.activate_account, name='activate_account'),
      re_path(r'^confirm/payment/(?P<id>\d+)/$', views.confirm_payment, name='confirm_payment'),
      re_path(r'^confirm/bid/(?P<id>\d+)/$', views.confirm_bid, name='confirm_bid'),
      re_path(r'^payment/done/', views.payment_done, name='payment')
]
