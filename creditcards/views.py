from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import CreditCardsSerializer 

class CreditCardView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = {
            'from_account': request.data.get('account'),
            'card_number': request.data.get('card_number'),
            'expiration_date': request.data.get('expiration_date'),
            'cvc': request.data.get('cvc')
        }

        serializer = CreditCardsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
