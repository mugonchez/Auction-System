from django.db import models
from catalog.models import Product
from django.conf import settings
from django.core.validators import RegexValidator

validate_number = RegexValidator(regex=r'^\+?1?\d{2,12}$',
                                 message='phone number must be entered in the format +254... up to 12 digits allowed')


class OrderDetails(models.Model):
    ADDRESS_OF_DELIVERY = (
        ('Ng', 'Nchiru CBD'),
        ('Am', 'Kianjai',),
        ('Rw', 'Kioni',),
        ('Up', 'Mascan'))
    specification_of_product = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)
    address_of_delivery = models.CharField(max_length=50, choices=ADDRESS_OF_DELIVERY, default='Nchiru CBD')
    phone_number = models.CharField(blank=True, validators=[validate_number], max_length=13, null=True)
    approved = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='order', on_delete=models.CASCADE, null=True)
    active = models.BooleanField(default=True)
    paid = models.BooleanField(default=False)
    confirm = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        total = sum(item.get_cost() for item in self.details.all())
        return total


class Order(models.Model):
    order = models.ForeignKey(OrderDetails, related_name='details', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='orders', on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)
    product = models.ForeignKey(Product, related_name='order_item', on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ('-quantity',)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity


class OrderNotification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='notification', on_delete=models.CASCADE)
    message = models.TextField()
    active = models.BooleanField(default=True)
    read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'message for {}'.format(self.user)
