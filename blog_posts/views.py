import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from django.views.decorators.csrf import csrf_exempt
from .models import User, Post, Comment
from .serializers import UserSerializer, PostSerializer, CommentSerializer

# Import Singleton classes
from singletons.logger_singleton import LoggerSingleton
from singletons.config_manager import ConfigManager


class UserListCreate(APIView):
    def get(self, request):
        logger = LoggerSingleton()  # Get the singleton logger instance
        try:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            logger.log("Fetched all users successfully")  # Log success
            return Response(serializer.data)
        except Exception as e:
            logger.error(f"Error fetching users: {str(e)}")  # Log error
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        logger = LoggerSingleton()  # Get the singleton logger instance
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.log(f"Created user {serializer.data['username']} successfully")  # Log success
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            logger.error("User creation failed: Invalid data")  # Log error
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostListCreate(APIView):
    def get(self, request):
        logger = LoggerSingleton()  # Get the singleton logger instance
        try:
            posts = Post.objects.all()
            serializer = PostSerializer(posts, many=True)
            logger.log("Fetched all posts successfully")  # Log success
            return Response(serializer.data)
        except Exception as e:
            logger.error(f"Error fetching posts: {str(e)}")  # Log error
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        logger = LoggerSingleton()  # Get the singleton logger instance
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.log(f"Created post successfully with ID: {serializer.data['id']}")  # Log success
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            logger.error("Post creation failed: Invalid data")  # Log error
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentListCreate(APIView):
    def get(self, request, post_id):
        logger = LoggerSingleton()  # Get the singleton logger instance
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            raise NotFound(detail="Post not found")
        
        comments = Comment.objects.filter(post=post)
        serializer = CommentSerializer(comments, many=True)
        logger.log(f"Fetched comments for post ID {post_id} successfully")  # Log success
        return Response(serializer.data)

    def post(self, request, post_id):
        logger = LoggerSingleton()  # Get the singleton logger instance
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            raise NotFound(detail="Post not found")
        
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=post)
            logger.log(f"Created comment for post ID {post_id} successfully")  # Log success
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            logger.error(f"Comment creation failed for post ID {post_id}: Invalid data")  # Log error
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def update_user(request, id):
    logger = LoggerSingleton()  # Get the singleton logger instance
    if request.method == 'PUT':
        try:
            # Parse the incoming JSON data
            data = json.loads(request.body)
            email = data.get('email')  # Get the email field

            # Try to fetch the user, and raise a NotFound error if the user does not exist
            user = User.objects.filter(id=id).first()
            if not user:
                raise NotFound(detail="User not found")  # Raise an error if no user found
            
            # Update the user's email and save the changes
            user.email = email
            user.save()

            logger.log(f"User {id} updated successfully")  # Log success
            return Response({'message': 'User updated successfully'}, status=status.HTTP_200_OK)
        except NotFound as e:
            logger.error(f"Error updating user {id}: {str(e)}")  # Log error
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)  # Handle NotFound exception
        except Exception as e:
            logger.error(f"Error updating user {id}: {str(e)}")  # Log error
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)  # Handle other exceptions


@csrf_exempt
def delete_user(request, id):
    logger = LoggerSingleton()  # Get the singleton logger instance
    if request.method == 'DELETE':
        try:
            user = User.objects.filter(id=id).first()
            user.delete()
            logger.log(f"User {id} deleted successfully")  # Log success
            return Response({'message': 'User deleted successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error deleting user {id}: {str(e)}")  # Log error
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
