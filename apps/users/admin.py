from django.contrib import admin
from apps.users.models import User
from django.core.mail import send_mail


class UserPermissions(admin.ModelAdmin):
    actions = ['send_mails']

    @admin.action(description='Send Mail')
    def send_mails(self, request, queryset):
        send_mail(subject='Test', message='Test Message', from_email=None, recipient_list=queryset.values_list('email', flat=True))



admin.site.register(User, UserPermissions)
