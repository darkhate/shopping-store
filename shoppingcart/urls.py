from django.conf.urls import url

from .views import data_view

urlpatterns = [
    url(r'^$', data_view ,name='list'),
]