from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models import Count
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, UpVoteSerializer


class PostViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = PostSerializer
    http_method_names = ['get', 'post', 'delete', 'put']
    queryset = Post.objects.annotate(num_up_votes=Count('up_votes')).order_by('-num_up_votes')

    def perform_create(self, serializer):
        serializer.save(author_name=self.request.user)

    def perform_destroy(self, serializer):
        obj = self.get_object()
        if obj.author_name == self.request.user:
            obj.delete()

    def perform_update(self, serializer):
        serializer.save(author_name=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = CommentSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(author_name=self.request.user)

    def perform_destroy(self, serializer):
        obj = self.get_object()
        if obj.author_name == self.request.user:
            obj.delete()

    def perform_update(self, serializer):
        serializer.save(author_name=self.request.user)


class UpVoteViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = UpVoteSerializer
    http_method_names = ['get', 'put',]

    def get_queryset(self):
        if self.kwargs:
            queryset = Post.objects.filter(pk=self.kwargs['pk'])
            return queryset
        return None

    def perform_update(self, serializer):
        obj = self.get_object()
        if self.request.user in obj.up_votes.all():
            obj.up_votes.remove(self.request.user)
        else:
            obj.up_votes.add(self.request.user)
