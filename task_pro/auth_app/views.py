
from rest_framework import generics
from rest_framework.response import Response
from .serializers import UserSerializer, User


class UserRegister(generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)
        return Response(data=serializer.errors, status=404)

class UserList(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request):
        obj = User.objects.all()
        serializer = UserSerializer(obj, many=True)
        return Response(data=serializer.data, status=200)

