from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^dashboard$', views.dashboard),
    url(r'^logout$', views.logout),
    url(r'^wish_items/(?P<id>\d+)$', views.show),
    url(r'^wish_items/(?P<id>\d+)/delete$', views.delete),
    url(r'^wish_items/(?P<id>\d+)/remove$', views.remove),
    url(r'^wish_items/(?P<id>\d+)/add$', views.add),
    url(r'^wish_items/create$', views.create),
    url(r'^new_item$', views.new_item)

]