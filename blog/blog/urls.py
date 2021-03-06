"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path

from blog.settings import MEDIA_ROOT
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
# import xadmin
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('xadmin/',xadmin.site.urls),
    path('', include('apps.myblog.urls', namespace='myblog')),
    path('article/', include('apps.article.urls', namespace='article')),
    path('mdeditor/', include('mdeditor.urls')),
    path('comment/',include('apps.comment.urls',namespace='comment')),
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
]

# if settings.DEBUG:
#     # static files (images, css, javascript, etc.)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
