from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.views import status

from .models import User


# Create your views here.
class UserViewSet(ViewSet):
    model = User

    def signup(self, request):
        return Response(status=status.HTTP_201_CREATED)

    def retrieve_profile(self, request):
        return Response(status=status.HTTP_200_OK)

    def update_profile(self, request):
        return Response(status=status.HTTP_201_CREATED)
