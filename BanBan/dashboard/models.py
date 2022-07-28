from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

#게시판
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    where = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    writeDate = models.DateTimeField(blank=True, null=True)
 
    def __str__(self):
        return self.title

#댓글
class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment