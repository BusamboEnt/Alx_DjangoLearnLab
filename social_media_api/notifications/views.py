from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from posts.models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

class NotificationListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        notifications = [{
            "actor": notification.actor.username,
            "verb": notification.verb,
            "target": str(notification.target),
            "timestamp": notification.timestamp,
            "read": notification.read
        } for notification in queryset]

        return Response(notifications)

class LikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        user = request.user

        # Prevent liking a post multiple times
        if Like.objects.filter(user=user, post=post).exists():
            return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Create the like
        like = Like.objects.create(user=user, post=post)

        # Create a notification for the post author
        Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb="liked your post",
            target_content_type=ContentType.objects.get_for_model(post),
            target_object_id=post.id
        )

        return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        user = request.user

        like = Like.objects.filter(user=user, post=post).first()
        if not like:
            return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)

      
        like.delete()

        return Response({"detail": "Post unliked successfully."}, status=status.HTTP_204_NO_CONTENT)
