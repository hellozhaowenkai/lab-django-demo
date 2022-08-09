from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from my_app.models import MyUser, Like, History


# Register your models here.


class MyAdminSite(admin.AdminSite):
    site_url = "/"


my_admin_site = MyAdminSite(name="my-admin")
my_admin_site.register(MyUser, UserAdmin)
my_admin_site.register([Like, History])
