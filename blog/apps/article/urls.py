from django.urls import path,include,re_path
from .views import ArticleView,ArticlesuibiView,SearchView,CategoryView,PhotoView,GiveLike

app_name = 'article'

urlpatterns = [
    re_path('article/(?P<article_id>\d+)/',ArticleView.as_view(),name='article'),
    path('articlesuibi/',ArticlesuibiView.as_view(),name='articlesuibi'),
    path('search/',SearchView.as_view(),name='search'),
    path('category/<int:pk>/',CategoryView.as_view(), name='category'),
    path('share/',PhotoView.as_view(),name='share'),
    path('give_like/', GiveLike, name='give_like'),



]
