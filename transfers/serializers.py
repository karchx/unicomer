from rest_framework import serializers
from .models import Transfers

class TransfersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfers 
        fields = ["from_account_id", "to_account_id", "amount"]
