from django.contrib import admin
from .models import DbForm, User
# Register your models here.
@admin.register(DbForm)
class ModelAdminDbForm(admin.ModelAdmin):
    list_display = ('First_name', 'Email', 'Phone')

@admin.register(User)
class UserModelForm(admin.ModelAdmin):
    list_display = ['name', 'email', 'site', 'password']
# admin.site.register(DbForm, ModelAdminDbForm)