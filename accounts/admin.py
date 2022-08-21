from django.contrib import admin

from accounts.models import User, Token

admin.site.register(User)
admin.site.register(Token)
# Register your models here.
