from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.views import status

from .models import Blog, BlogPost
from .serializers import BlogSerializer, BlogPostSerialzier
from .methods import is_user_blog

# Create your views here.
class BlogViewSet(ViewSet):
    serializer_class = BlogSerializer
    query_set = Blog.objects.all()

    def list_blog(self, request):
        blogs = Blog.objects.all()
        serialzier = BlogSerializer(blogs, many=True)
        return Response(serialzier.data, status=status.HTTP_200_OK)

    def create_blog(self, request):
        user = request.user
        if user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        data = {
            "user": user.id,
            "name": request.data.get("name", ""),
        }
        serializer = BlogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve_blog(self, request, blog_name):
        blog = get_object_or_404(Blog, name=blog_name)
        serialzier = BlogSerializer(blog)
        return Response(serialzier.data, status=status.HTTP_200_OK)

    def update_blog(self, request, blog_name):
        user = request.user
        if user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        blog = get_object_or_404(Blog, name=blog_name)
        if not is_user_blog(user, blog):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        data = {
            "user": user.id,
            "name": request.data.get("name", blog.name),
        }
        serializer = BlogSerializer(blog, data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class BlogPostViewSet(ViewSet):
    serializer_class = BlogPostSerialzier
    query_set = BlogPost.objects.all()

    def list_post(self, request, blog_name):
        blog = get_object_or_404(Blog, name=blog_name)
        blog_posts = BlogPost.objects.filter(blog=blog)
        serializer = BlogPostSerialzier(blog_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create_post(self, request, blog_name):
        user = request.user
        if user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        blog = get_object_or_404(Blog, name=blog_name)
        data = {
            "blog": blog.id,
            "title": request.data.get("title", ""),
            "content": request.data.get("content", ""),
        }
        serializer = BlogPostSerialzier(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve_post(self, request, blog_name, post_id):
        blog = get_object_or_404(Blog, name=blog_name)
        post = get_object_or_404(BlogPost, blog=blog.id, id=post_id)
        serializer = BlogPostSerialzier(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update_post(self, request, blog_name, post_id):
        user = request.user
        if user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        blog = get_object_or_404(Blog, name=blog_name)
        if not is_user_blog(user, blog):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        post = get_object_or_404(BlogPost, blog=blog.id, id=post_id)
        data = {
            "blog": blog.id,
            "title": request.data.get("title", ""),
            "content": request.data.get("content", ""),
        }
        serializer = BlogPostSerialzier(post, data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy_post(self, request, blog_name, post_id):
        user = request.user
        if user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        if not is_user_blog(user, blog):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        blog = get_object_or_404(Blog, name=blog_name)
        post = get_object_or_404(BlogPost, blog=blog.id, id=post_id)
        post.delete()
        return Response(status.HTTP_204_NO_CONTENT)
