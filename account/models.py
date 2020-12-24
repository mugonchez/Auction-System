from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


class Terms(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return 'Checked by {}'.format(self.user)






