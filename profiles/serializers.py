from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from profiles.models import CarerProfile, StudentProfile


class StudentProfileSerializer(ModelSerializer):
    user = serializers.ReadOnlyField(source='user.pk')

    class Meta:
        model = StudentProfile
        fields = '__all__'


class CarerProfileSerializer(ModelSerializer):
    user = serializers.ReadOnlyField(source='user.pk')

    class Meta:
        model = CarerProfile
        fields = '__all__'
