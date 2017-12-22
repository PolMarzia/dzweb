from mainsite.views import *
from django.conf.urls import url
from mainsite import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.mainpage, name='index'),
    url(r'^main/$', views.mainpage, name='index'),
    url(r'^skazki_babushki_larisy/$', views.skazki, name='skazki_lar'),
    url(r'^skazki_unih_darovanii/$', views.skazki_dar, name='skazki_dar'),
    url(r'^risunki/$', views.risunki, name='risunki'),
    url(r'^admin_page/$', views.admin_page, name='admin_page'),
    url(r'^admin_page_skazki/$', views.admin_page_skazki, name='admin_page_skazki'),
    url(r'^add_skazka/$', views.add_skazka, name='add_skazka'),
    url(r'^delete_skazka/(?P<id_skazka>\d+)$$', views.delete_skazka, name='delete_skazka'),
    url(r'^change_skazka/(?P<id_skazka>\d+)$', views.change_skazka, name="change_skazka"),
]