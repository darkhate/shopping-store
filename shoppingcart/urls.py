from django.conf.urls import url

from .views import data_detail_view,data_view

urlpatterns = [
    url(r'^$', data_view ,name='list'),
    url(r'^(?P<id>\d+)/$', data_detail_view ,name='detail'),
]