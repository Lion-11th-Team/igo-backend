from django.contrib.auth import get_user_model
from django.utils import timezone

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from programs.models import Program


class ProgramSerializer(ModelSerializer):
    author = serializers.ReadOnlyField(source='author.pk')
    subscriber = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    status = serializers.SerializerMethodField()

    class Meta:
        model = Program
        fields = '__all__'

    def get_status(self, obj):
        if obj.is_registing:
            return 'now'
        elif timezone.now() < obj.regist_start_at:
            return 'before'
        else:
            return 'done'
