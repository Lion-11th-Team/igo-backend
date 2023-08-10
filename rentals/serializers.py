from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from rentals.models import Rental, RentalContract


class RentalListRetrieveSerializer(ModelSerializer):
    class Meta():
        model = Rental
        fields = '__all__'


class RentalContractSerializer(ModelSerializer):
    class Meta():
        model = RentalContract
        fields = '__all__'
