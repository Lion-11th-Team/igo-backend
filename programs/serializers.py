from django.contrib.auth import get_user_model
from django.utils import timezone

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from profiles.serializers import AddressSerializer

from programs.models import Program


class ProgramSerializer(ModelSerializer):
    author = serializers.ReadOnlyField(source='author.pk')
    subscriber = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    activity_status = serializers.ReadOnlyField()
    regist_status = serializers.ReadOnlyField()
    address = AddressSerializer(many=False, read_only=True)

    class Meta:
        model = Program
        fields = '__all__'
