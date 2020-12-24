from django.db import models
from django.conf import settings


class Payment(models.Model):
    code = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    active = models.BooleanField()

    def __str__(self):
        return self.code


class Balance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    credit_number = models.IntegerField()
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    security_code = models.IntegerField(null=True)



