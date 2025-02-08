from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.get_posts, name='get_posts'),  # GET request to retrieve all posts
    path('posts/create/', views.create_post, name='create_post'),  # POST request to create a new post
    path('posts/<int:post_id>/comments/', views.get_comments, name='get_comments'),  # GET request to retrieve comments for a specific post
    path('posts/<int:post_id>/comments/create/', views.create_comment, name='create_comment'),  # POST request to create a comment for a specific post
]
