"""Belajar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, re_path, include
from Belajar import views as view_belajar
from publishing import views as view_publishing

urlpatterns = [
    path( '', view_belajar.home, name='home'), # root url, home adalah nama link
    path( 'hello-world', view_belajar.hello_world, name='hello_world'), # hello_world adalah nama link
    path( 'index1', view_belajar.indek1, name='indeksatu'),
    path( 'publishing/', view_publishing.index, name='home_publishing'),
    path( 'base-demo', view_belajar.base_demo, name='base_demo'),
    path( 'publisher-list', view_publishing.list_publisher, name='publisher-list'),
    #re_path( r'^publisher/(?P<id>[0-9]{4})$', view_publishing.publisher_details, name='publisher_details'),
    re_path( r'^publisher/(?P<id>\d+)/$', view_publishing.publisher_details, name='publisher_details'),
    #path( 'publisher/<int:id>/', view_publishing.publisher_details, name='publisher_details'),
    path( 'publishing-view/', include('publishing_view.urls')),
    path( 'contoh-static/', include('contoh_static.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # add by spd for testing the media
