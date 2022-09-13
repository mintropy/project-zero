from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.views import status

from .models import User
from .serializers import UserSerializer


def validate(type: str, string: str) -> bool:
    if type == "username" and 2 > len(string) > 10:
        return False
    if type == "password" and 6 > len(string) > 20:
        return False
    if all(
        [
            any([s.isdigit() for s in string]),
            any([s.isupper() for s in string]) or any([s.islower() for s in string]),
        ]
    ):
        return True
    return False


# Create your views here.
class UserViewSet(ViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def signup(self, request):
        data = {
            "username": request.data.get("username", ""),
            "password": request.data.get("password", ""),
        }
        if not validate("username", data["username"]) or not validate(
            "password", data["password"]
        ):
            return Response(
                data={"error": "validation error"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serialzier = UserSerializer(data=data)
        if serialzier.is_valid():
            serialzier.save()
            return Response(data=serialzier.data, status=status.HTTP_201_CREATED)
        return Response(data=serialzier.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve_profile(self, request):
        user = request.user
        if user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = UserSerializer(instance=user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update_profile(self, request):
        user = request.user
        if user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
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
