from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Post

admin.site.register(User, UserAdmin)
UserAdmin.fieldsets += (("Custom fields", {"fields":('name','rank')}),)

admin.site.register(Post)