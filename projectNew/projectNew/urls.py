from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from billingapp .views import Getinput,Add,Food
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^billingapp/Getinput$',Getinput.as_view()),
    url(r'^billingapp/Add$',Add.as_view()),
    url(r'^billingapp/Food$',Food.as_view()),
]