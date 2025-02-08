from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel URL
    path('api-auth/', include('rest_framework.urls')),  # API authentication
    path('posts/', include('blog_posts.urls')),  # Include blog_posts URLs here
    path('', home, name='home'),  # Home URL
]
