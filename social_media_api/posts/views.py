from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, filters
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        following_users = self.request.user.following.all()  # Get followed users
        return Post.objects.filter(author__in=following_users).order_by('-created_at')  # Explicit filtering

from rest_framework import status, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404  # Correct import from django.shortcuts
from .models import Post, Like
from notifications.models import Notification
from rest_framework.decorators import api_view, permission_classes

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    # Correctly use get_object_or_404 here
    post = get_object_or_404(Post, pk=pk)
    
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if created:
        # Generate a notification when a post is liked
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            target=post
        )
        return Response({"message": "Post liked!"}, status=status.HTTP_201_CREATED)
    else:
        return Response({"message": "You have already liked this post!"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    # Correctly use get_object_or_404 here as well
    post = get_object_or_404(Post, pk=pk)

    like = Like.objects.filter(user=request.user, post=post)

    if like.exists():
        like.delete()
        return Response({"message": "Post unliked!"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "You haven't liked this post!"}, status=status.HTTP_400_BAD_REQUEST)
