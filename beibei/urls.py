from django.conf.urls import url

from beibei import views

urlpatterns = [
    url(r'^$', views.index),
]