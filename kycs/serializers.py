from rest_framework import serializers
from .models import Kyc

class KycSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kyc
        fields = [
            'id',
            'location', 
            'customer_name', 
            'amount_paid', 
            'volume_dispensed', 
            'status'
        ]

