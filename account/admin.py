from django.contrib import admin
from.models import Profile, Terms


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']
admin.site.register(Profile, ProfileAdmin)


class TermsAdmin(admin.ModelAdmin):
    list_display = ['user', 'checked']
admin.site.register(Terms, TermsAdmin)

