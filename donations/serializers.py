from rest_framework.serializers import ModelSerializer
from .models import Donation

class DonationSerializer(ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'