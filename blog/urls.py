from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'(\d)+', views.detail, name='detail'),
    url('', views.allblogs, name='allblogs')
]
