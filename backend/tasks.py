from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import Post


@shared_task
def reset_up_votes():
    post_objs = Post.objects.all()
    for post_obj in post_objs:
        post_obj.up_votes.clear()
