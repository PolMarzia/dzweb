from mainsite.views import *
from django.conf.urls import url
from mainsite import views

urlpatterns = [
    url(r'^$', views.mainpage, name='index'),
    url(r'^main/', views.mainpage, name='index'),
    url(r'^skazki_babushki_larisy/', views.skazki, name='skazki_lar'),
    url(r'^skazki_unih_darovanii/', views.skazki_dar, name='skazki_dar'),
    url(r'^risunki/', views.risunki, name='risunki')
]