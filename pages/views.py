from django.shortcuts import render

def writeHello():
    return "Hello World!"
# Create your views here.

def Home_Page(request):
    return render(request, template_name = "home.html")

def Blog_Page(request):
    return render(request, template_name = "blog.html")

def Contact_Page(request):
    return render(request, template_name = "contact.html")

def About_Page(request):
    return render(request, template_name = "about.html")

def Posts_Page(request):
    return render(request, template_name = "posts.html")