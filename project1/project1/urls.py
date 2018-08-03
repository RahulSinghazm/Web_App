from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from app1 import views

urlpatterns = [
     path('admin/',admin.site.urls),
     url(r'^app1/input',views.input,name='input'),
     url(r'^app1/add',views.add,name='add'),
]
