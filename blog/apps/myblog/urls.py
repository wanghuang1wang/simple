from django.urls import path,include
from .views import Index


app_name = 'myblog'
urlpatterns = [
    path('',Index.as_view(),name="index"),


]
