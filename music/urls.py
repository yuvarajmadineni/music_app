from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, ListView
from . import views
from django.conf.urls import url
# from music.views import EnglishAlbumView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('main/',TemplateView.as_view(template_name='main.html'),name='main'),
    url(r'^telugu/$',views.telugu,name='telugu'),
    url(r'telugu/(?P<pk>[0-9]+)/$', views.detail, name='song'),
    url(r'^english/$', views.english,name='english'),
    url(r'^english/(?P<pk>[0-9]+)/$', views.detail, name='song'),
    url(r'^malayalam/$',views.malayalam,name='malayalam'),
    url(r'malayalam/(?P<pk>[0-9]+)/$', views.detail, name='song'),
    url(r'^favorite/$',views.favorite,name='favorite'),
    url(r'^favorite/(?P<pk>[0-9]+)/$', views.detail, name='song'),
    path('home/',views.userinfo,name='home'),
    path('newalbum/',views.addnewalbum, name='addnewalbum'),
    path('newsong/',views.addnewsong, name='addnewsong'),
    path('userprofile/',views.profileuser, name='profileuser'),
]
