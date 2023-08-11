from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from .models import Donation
from .serializers import DonationSerializer
from rest_framework.decorators import action

class DonationViewSet(ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
    
    @action(detail=True, methods=('POST',))
    def create(self, request, *args, **kwargs):
        data = request.data
        donation_record= Donation(**data)
        donation_record.save()
        donation_serializer = DonationSerializer(donation_record)
        return Response(donation_serializer.data)