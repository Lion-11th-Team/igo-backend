from rest_framework.serializers import ModelSerializer

from profiles.models import Address
from .models import Donation


class DonationSerializer(ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address_inst = Address.objects.create(**address_data)
        donation_inst = Donation.objects.create(
            **validated_data, address=address_inst)
        return donation_inst
