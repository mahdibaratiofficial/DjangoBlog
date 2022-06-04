from django.shortcuts import render
from posts.models import Post

def writeHello():
    return "Hello World!"
# Create your views here.

def Home_Page(request):
    posts=Post.objects.all()
    return render(request, template_name = "home.html",context={'posts':posts})

def Blog_Page(request):
    posts=Post.objects.all()
    return render(request, template_name = "blog.html",context={'posts':posts})

def Contact_Page(request):
    return render(request, template_name = "contact.html")

def About_Page(request):
    return render(request, template_name = "about.html")

def Posts_Page(request,pk):
    post=Post.objects.get(pk=pk)
    posts=Post.objects.all()
    return render(request, template_name = "posts.html",context={'post':post,'posts':posts})