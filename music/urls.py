from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, ListView
from . import views
from django.conf.urls import url
# from music.views import EnglishAlbumView

urlpatterns = [
    # path('',TemplateView.as_view(template_name='home.html'),name='home'),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('main/',TemplateView.as_view(template_name='main.html'),name='main'),
    url(r'^telugu/(?P<album_id>[0-9]+)/$',TemplateView.as_view(template_name='telugu.html'),name='telugu'),
    url(r'^english/', views.index,name='english'),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^$', views.index, name='index'),
]
