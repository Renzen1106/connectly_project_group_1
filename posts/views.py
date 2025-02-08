from django.http import JsonResponse

# View for getting all users
def get_users(request):
    users = [
        {"id": 1, "username": "testuser", "email": "testuser@example.com"}
    ]
    return JsonResponse(users, safe=False)

# View for creating a new user
def create_user(request):
    return JsonResponse({"message": "User created successfully"})

# View for getting all posts
def get_posts(request):
    posts = [
        {"id": 1, "content": "This is a test post", "author_id": 1}
    ]
    return JsonResponse(posts, safe=False)

# View for creating a new post
def create_post(request):
    return JsonResponse({"message": "Post created successfully"})
