from django.conf.urls import include, url
from . import views

urlpatterns =[
    url(r'^$', views.index, name="index"),
    url(r'^process_money$', views.process_money, name="ninja-gold"),
    url(r'^clear$', views.clear)
]
