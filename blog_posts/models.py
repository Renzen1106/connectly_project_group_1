from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)  # Ensure unique username
    email = models.EmailField(unique=True)  # Ensure unique email
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the date when the user is created

    def __str__(self):
        return self.username


class Post(models.Model):
    content = models.TextField()  # Content of the post
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)  # Link to the User model
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the date when the post is created

    def __str__(self):
        return f"Post by {self.author.username} at {self.created_at}"


class Comment(models.Model):
    text = models.TextField()  # Text content of the comment
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)  # Link to the User model
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)  # Link to the Post model
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the date when the comment is created

    def __str__(self):
        return f"Comment by {self.author.username} on Post {self.post.id}"
