from rest_framework.serializers import ModelSerializer

from profiles.models import CarerProfile, StudentProfile


class StudentProfileSerializer(ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'


class CarerProfileSerializer(ModelSerializer):
    class Meta:
        model = CarerProfile
        fields = '__all__'
