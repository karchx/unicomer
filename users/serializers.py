from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'name', 'lastname', 'password']

    def create(self, validated_data):
        user = CustomUser.objects.create(name = validated_data['name'],
                                         lastname = validated_data['lastname'],
                                         email = validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()

        return user
