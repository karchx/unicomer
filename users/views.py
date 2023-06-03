from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from .models import CustomUser


class Register(APIView):
    def post(self, request):
        serializers = UserSerializer(data = request.data)

        if not serializers.is_valid():
            return Response({'status': 403, 'errors': serializers.errors,
                             'message': 'Some wrong error'})

        serializers.save()
        
        user = CustomUser.objects.get(email = serializers.data['email'])
        token_obj, _ = Token.objects.get_or_create(user=user)

        return Response({'status': 201, 'payload': serializers.data, 'token':
                         str(token_obj), 'message':
                         'User created'}, status=status.HTTP_201_CREATED)

class LoginAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        print(user)
        if user:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
