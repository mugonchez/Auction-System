from django.shortcuts import render, get_object_or_404
from .models import Order
from orders.models import OrderNotification
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from .email_notification import sending_email
from catalog.models import Product
from .stock import get_stock


@login_required
def create_order(request):
    order_notifications = OrderNotification.objects.filter(user=request.user, active=True)
    notification_count = order_notifications.count()
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart:
                Order.objects.create(order=order,
                                     user=request.user,
                                     product=item['product'],
                                     price=item['price'],
                                     quantity=item['quantity'])
            cart.clear()
            sending_email(request, order.id)
            return render(request, 'orders/order_created.html', {'order': order,
                                                                 'notification_count': notification_count})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order_create.html', {'cart': cart, 'form': form})




