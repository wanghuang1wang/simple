from django.contrib import admin
from .models import *

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['avatar','qq','mobile']

#注册 否则 simpleui 无法显示
admin.site.register(UserProfile,UserProfileAdmin)



