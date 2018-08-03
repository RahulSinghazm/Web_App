from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from app3.views import GetInput,PostInput,Add
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^app3/getinput',GetInput.as_view()),
    url(r'^app3/postinput',PostInput.as_view()),
    url(r'^app3/add',Add.as_view()),
]
