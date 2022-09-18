from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.views import status

from .models import Blog, BlogPost
from .serializers import BlogSerializer, BlogPostSerialzier

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
    model = BlogPost

    def list_post(self, request):
        return Response(status=status.HTTP_200_OK)

    def create_post(self, request):
        return Response(status=status.HTTP_201_CREATED)

    def retrieve_post(self, request):
        return Response(status=status.HTTP_200_OK)

    def update_post(self, request):
        return Response(status=status.HTTP_201_CREATED)

    def destroy_post(self, request):
        return Response(status.HTTP_204_NO_CONTENT)
