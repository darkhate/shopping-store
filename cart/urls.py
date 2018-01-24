"""cart URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from .views import Home,redirect_where
from shoppingcart.views import data_view,render_where

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Home , name='home'),
    url(r'^redirect/$', redirect_where , name='redirect'),
    url(r'^data/', include('shoppingcart.urls')),
    url(r'^post/$', data_view),
    url(r'^render/$', render_where , name='render'),
]
