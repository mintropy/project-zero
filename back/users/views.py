from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.views import status

from .models import User
from .serializers import UserSerializer


# Create your views here.
class UserViewSet(ViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def signup(self, request):
        data = {
            "username": request.data.get("username", ""),
            "password": request.data.get("password", ""),
        }
        serialzier = UserSerializer(data=data)
        if serialzier.is_valid():
            serialzier.save()
            return Response(data=serialzier.data, status=status.HTTP_201_CREATED)
        return Response(data=serialzier.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve_profile(self, request):
        user = User.objects.get(username="admin")
        serializer = UserSerializer(instance=user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update_profile(self, request):
        user = User.objects.get(username="admin")
        data = {
            "username": user.username,
            "password": user.password,
            "email": request.data.get("email", ""),
        }
        serializer = UserSerializer(instance=user, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
