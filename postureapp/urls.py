from django.conf.urls import url
from rest_framework import routers

from . import views


urlpatterns = [
    url(r'^upload$', views.index, name='index'),
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^about$', views.about, name='about'),
    url(r'^report$', views.report, name='report'),
    url(r'^team$', views.team, name='team'),
               #url(r'^api$', views.user_list, name='user_list'),
    url(r'^getrecommendation/$', views.getrecommendation),
#    url(r'^upload/(?P<filename>[^/]+)$', FileUploadView.as_view()),
]
