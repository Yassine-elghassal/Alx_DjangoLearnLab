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


from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404  # ✅ Make sure this is imported
from .models import Post, Like
from notifications.models import Notification
from .serializers import PostSerializer

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # ✅ Using get_object_or_404 to fetch the post
        post = generics.get_object_or_404(Post, pk=pk)  

        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            like.delete()
            return Response({"message": "Like removed"}, status=status.HTTP_204_NO_CONTENT)

        # ✅ Ensure notification is created when someone likes a post
        if request.user != post.author:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked",
                target=post
            )

        return Response({"message": "Post liked"}, status=status.HTTP_201_CREATED)
