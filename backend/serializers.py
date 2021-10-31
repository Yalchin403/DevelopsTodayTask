from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'link', 'author_name', 'up_votes')
        read_only_fields = ('id', 'up_votes')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'content', 'post', 'author_name')
        read_only_fields = ('id',)


class UpVoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'up_votes')
        read_only_fields = ('id',)
