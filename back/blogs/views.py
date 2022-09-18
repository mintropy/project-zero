from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.views import status

from .models import Blog, BlogPost
from .serializers import BlogSerializer, BlogPostSerialzier

# Create your views here.
class BlogViewSet(ViewSet):
    model = Blog

    def list_blog(self, request):
        return Response(status=status.HTTP_200_OK)

    def create_blog(self, request):
        return Response(status=status.HTTP_201_CREATED)

    def retrieve_blog(self, request):
        return Response(status=status.HTTP_200_OK)

    def update_blog(self, request):
        return Response(status=status.HTTP_201_CREATED)


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
