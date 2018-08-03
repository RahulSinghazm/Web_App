from django.conf.urls import url
from django.contrib import admin
from app2 import views
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^app2/getinput',views.getinput,name='input'),
    url(r'^app2/postinput',views.postinput,name='input'),
    url(r'^app2/add',views.add,name='add'),
]
