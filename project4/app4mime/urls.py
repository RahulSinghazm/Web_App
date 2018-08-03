from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from app4mime import views
app_name='mimeapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^html$',views.htmlview,name='htmlview'),
    url(r'^xml$',views.xmlview,name='xmlview'),
]