from django.db import models

from users.models import User

# Create your models here.
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name="blogs", on_delete=models.PROTECT)
    name = models.CharField(max_length=20, unique=True)


class BlogPost(models.Model):
    id = models.AutoField(primary_key=True)
    blog = models.ForeignKey(Blog, related_name="posts", on_delete=models.PROTECT)
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
