from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import feed
from . import views

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls

urlpatterns = [
    path('feed/', feed, name='feed'),
     path('posts/<int:post_id>/like/', views.like_post, name='like_post'),
    path('posts/<int:post_id>/unlike/', views.unlike_post, name='unlike_post'),
]
