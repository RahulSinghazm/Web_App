from django.conf.urls import url
from . import views
app_name='app6product'
urlpatterns=[
    url(r'^$',views.input,name='input'),
    url(r'^insert$',views.insert,name='insert'),
    url(r'^display$',views.display,name='display'),
]