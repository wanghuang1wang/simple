from django.contrib import admin

# Register your models here.
from .models import *
class CommentAdmin(admin.ModelAdmin):
    list_display = ['ariticle','comment_desc','comment_time']

admin.site.register(Comment, CommentAdmin)