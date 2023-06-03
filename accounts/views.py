from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import AccountsSerializer
from .models import Accounts

class Accounts(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        account_id = request.query_params["account_id"]
        account_instance = Accounts.objects.all()

        return Response({'account': account_instance})

    def post(self, request):
        data = {
              'owner': request.user.id,
              'balance': request.data.get('currency'),
              'currency': request.data.get('currency'),
         }

        serializer = AccountsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
