from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, LikePostView, UnlikePostView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', views.FeedViewSet.as_view({'get': 'list'}), name='feed'),
    path('<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
    path('post/<int:pk>/like/', views.like_post, name='like_post'),
    path('post/<int:pk>/unlike/', views.unlike_post, name='unlike_post'),
]
