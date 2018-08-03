from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
class GetInput(View):
    def get (self,request):
        return render(request,'getinput.html')

class PostInput(View):
    def post(self, request):
        return render(request, 'postinput.html')
class Add (View):
    def get(self,request):
        try:
            a=request.GET['t1']
            x=int(a)
            b=request.GET['t2']
            y=int(b)
            z=x+y
            return HttpResponse("<html><body bgcolor=blue><h1>Sum is : "+str(z)+" </h1></body></html>")
        except(ValueError):
            return HttpResponse("Invalid input")
    def post(self,request):
        try:
            a=request.POST['t1']
            x=int(a)
            b=request.POST['t2']
            y=int(b)
            z=x+y
            return HttpResponse("<html><body bgcolor=blue><h1>Sum is : "+str(z)+" </h1></body></html>")
        except(ValueError):
            return HttpResponse("Invalid input")
# Create your views here.
