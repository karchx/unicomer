from rest_framework import serializers
from .models import CreditCard

class CreditCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = ["from_account", "card_number", "expiration_date", "cvc"]
