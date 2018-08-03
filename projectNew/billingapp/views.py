from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
class Getinput(View):
    def get(self,request):
        return render(request,'base.html')
class Add(View):
    def get(self,request):
        m1=int(request.GET['t1'])
        m2=int(request.GET['t2'])
        m3= int(request.GET['t3'])
        m4= int(request.GET['t4'])
        m5= int(request.GET['t5'])
        m6= int(request.GET['t6'])
        m=str(m1*30+m2*30+m3*30+m4*30+m5*30+m6*30)
        return HttpResponse("<html><body bgcolor='pink'><h1>One month total money expence:"+m+"</h1></body></html")
class Food(View):
    def get(self,request):
        tfood=int(request.GET['s1'])
        f = int(request.GET['s2'])
        perfrnd=str(tfood/f)
        return HttpResponse("<html><body  bgcolor='yellow'><h1>Total amount on per friend:"+perfrnd+"</h1></body></html")
