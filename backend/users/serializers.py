from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def save(self):
        return User.objects.create_user(username=self.validated_data.get('username'), password=self.validated_data.get('password'))
        