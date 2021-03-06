"""expo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from hello.engin_menu import PcMenu
#from expo_cms.engin_menu import CMSMenu
from helpers.case.simcms.views import cms_view

from helpers.authuser.engin_view import AuthEngine

from django.views.generic import RedirectView 
from helpers.authuser import urls as authuser_urls
from expolink import views as expo_views

urlpatterns = [
    
    url(r'^index/?$',expo_views.Home.as_view()),
     url(r'^p/zhanxun/?$',expo_views.Zhanxun.as_view()),
    url(r'^p/3d/?$',expo_views.D3.as_view()),
    url(r'^p/vr/?$',expo_views.VR.as_view()),
    url(r'^p/fullscreen/?$',expo_views.FullScreen.as_view()),
    
    url(r'^p/zhanxun2/?$',expo_views.Zhanxun2.as_view()),
    
    
    
    
    url(r'^admin/', admin.site.urls),
    #url(r'^accounts/',include(authuser_urls)),
    
    url(r'^accounts/([\w\.]+)/?$',AuthEngine.as_view(),name=AuthEngine.url_name),
    #^articles/(?P<year>[0-9]{4})/$', views.year_archive
    url(r'^cms/(?P<name>\w+)/$', cms_view), 
    #url(r'^cms/([\w\.]+)/?$',CMSMenu.as_view(),name=CMSMenu.url_name),
    
    
    url(r'^d/',include('helpers.director.urls'),name='director'),
    url(r'^pc/([\w\.]+)/?$',PcMenu.as_view(),name=PcMenu.url_name),
    url(r'^pc/?$',RedirectView.as_view(url='/pc/home')),
    url(r'^$',RedirectView.as_view(url='/index')) ,
]



if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)