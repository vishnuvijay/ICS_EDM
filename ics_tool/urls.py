from django.conf.urls import url
from django.contrib.auth import views as auth_views


from . import views

app_name='ics_tool'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
