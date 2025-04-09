from rest_framework import viewsets, permissions, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Post, Comment
from accounts.models import CustomUser
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = Post.objects.all()
        title = self.request.query_params.get('title', None)
        content = self.request.query_params.get('content', None)
        if title:
            queryset = queryset.filter(title__icontains=title)
        if content:
            queryset = queryset.filter(content__icontains=content)
        return queryset

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        post = Post.objects.get(id=self.kwargs['post_id'])
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_id'])

class FeedViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        user = request.user
        followed_users = user.following.all()  
        posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')  # Get posts from followed users
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
class UserFeedView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]  

    def get_queryset(self):
        user = self.request.user
        
        following_users = user.following.all()
        
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        return posts

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)    