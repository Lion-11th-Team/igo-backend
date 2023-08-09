from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from rentals.models import Rental


class RentalListRetrieveSerializer(ModelSerializer):
    class Meta():
        model = Rental
        fields = '__all__'
