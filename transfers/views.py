from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import TransfersSerializer
from accounts.models import Accounts

class Transfers(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] 

    def post(self, request):
        user_id = request.user.id
        data = {
           'from_account_id': request.data.get('from'),
           'to_account_id': request.data.get('to'),
           'amount': request.data.get('amount')
        }

        serializer = TransfersSerializer(data=data) 
        if serializer.is_valid():
            serializer.save()
            self.debit(request.data.get('amount'), request.data.get('from'),
                       user_id)

            self.accredit(request.data.get('amount'), request.data.get('to'))

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def debit(self, amount, account_id, user_id): 
        account_obj = Accounts.objects.get(id=account_id,owner_id=user_id)
        if account_obj.currency < amount:
            return Response({'message': 'insufficient money'}, status=status.HTTP_400_BAD_REQUEST)

        account_obj.currency = account_obj.currency - amount
        account_obj.save()


    def accredit(self, amount, account_id): 
        account_obj = Accounts.objects.get(id=account_id)

        account_obj.currency = account_obj.currency + amount
        account_obj.save()

