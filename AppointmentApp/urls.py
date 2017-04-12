from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^calendar', views.calendar),
    url(r'^home', views.home),
]