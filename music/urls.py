from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('',TemplateView.as_view(template_name='home.html'),name='home'),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('main/',TemplateView.as_view(template_name='main.html'),name='main'),
    path('telugu/',TemplateView.as_view(template_name='telugu.html'),name='telugu'),
    # path('tamil/',TemplateView.as_view(template_name='tamil.html'),name='tamil'),
    path('english/',TemplateView.as_view(template_name='english.html'),name='english'),
    # url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),
    # url(r'^create_album/$', views.create_album, name='create_album'),
    # url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),
]
