from django.contrib.auth import get_user_model
from users.serializers import UserSerializer
from rest_framework.response import Response

# Create your views here.
from rest_framework import generics
User = get_user_model()

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, username):
        try:
            user = User.objects.get(username=username)
            serializer = UserSerializer(user)
        except Exception as e:
            return Response(str(e), status=404)
        return Response(serializer.data, status=200)

    def update(self, request, username):
        try:
            user = User.objects.get(username=username)
            user.username = request.data.get('username')
            password = request.data.get('password')
            if not user.check_password(password):
                user.set_password(password)
            user.save()
        except Exception as e:
            return Response(str(e), status=400)
        return Response(UserSerializer(user).data, status=200)

    def destroy(self, request, username):
        try:
            user = User.objects.get(username=username)
            user.delete()
            return Response(status=204)
        except Exception as e:
            return Response(str(e), status=404)
        