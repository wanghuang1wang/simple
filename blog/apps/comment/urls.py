# -*- coding: utf-8 -*-
#author: Xin Yue
#FileName: urls
#time: 2020/6/6 22:44

from django.urls import path,include
from .views import CommentView


app_name = 'comment'
urlpatterns = [
    path('',CommentView.as_view(),name="comment"),


]