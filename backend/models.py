from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    link = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    up_votes = models.ManyToManyField(User, related_name="up_votes")
    author_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"{self.author_name}'s comment on {self.post}"
