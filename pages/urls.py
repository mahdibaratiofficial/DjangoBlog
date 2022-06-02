from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home_Page, name = 'home'),
    path('home/', views.Home_Page, name = 'home'),
    path('blog/', views.Blog_Page, name = 'blog'),
    path('posts/', views.Posts_Page, name = 'posts'),
    path('contact/', views.Contact_Page, name = 'contact'),
    path('about/', views.About_Page, name = 'about'),
]