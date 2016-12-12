from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='indice'),

    url(r'^unidade/list$', views.unidade_list, name='unidade_list'),
    url(r'^unidade/detail/(?P<pk>\d+)$', views.unidade_detail, name='unidade_detail'),
    url(r'^unidade/new/$',views.unidade_new,name='unidade_new'),
    url(r'^unidade/update/(?P<pk>\d+)$',views.unidade_update,name='unidade_update'),
    url(r'^unidade/delete/(?P<pk>\d+)$',views.unidade_delete,name='unidade_delete'),

]