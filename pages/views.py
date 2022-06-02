from django.shortcuts import render

def writeHello():
    return "Hello World!"
# Create your views here.

def welcome(request):
    return render(request,template_name="welcome.htm")


def home(request):
    return render(request,'home.htm', {'writeHello': 'writeHello'})
