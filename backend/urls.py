from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('posts', views.PostViewSet, basename='posts')
router.register('upvote', views.UpVoteViewSet, basename='upvote')
router.register('comments', views.CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
]