from django.contrib import admin
# from django.contrib.admin import ModelAdmin
from .models import *

from .models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'desc', 'image','click_count', 'is_recommend', 'date_publish','like_click']
    search_fields = ['title']
    list_editable = ['click_count']
    list_filter = ['title']  #过滤器



class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ['name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class PhotoAlbumAdmin(admin.ModelAdmin):
    list_display = ['title','desc','click_count','is_recommend','date_publish']


class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ['name']


class FriendsChainAdmin(admin.ModelAdmin):
    list_display = ['name','url']

#注册 否则 simpleui 无法显示
admin.site.register(Article,ArticleAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(PhotoAlbum,PhotoAlbumAdmin)
admin.site.register(ArticleTag,ArticleTagAdmin)
admin.site.register(FriendsChain,FriendsChainAdmin)
