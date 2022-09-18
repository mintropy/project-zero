from rest_framework import serializers

from .models import Blog, BlogPost


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog


class BlogPostSerialzier(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
