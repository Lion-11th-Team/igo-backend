from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action

from accounts.serializer import UserSerializer
from profiles.models import CarerProfile, StudentProfile
from profiles.serializers import CarerProfileSerializer, StudentProfileSerializer
from rentals.models import RentalContract
from rentals.serializers import RentalContractSerializer


class AccountCreateRetrieveViewSet(CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = get_user_model().objects.all()
    # serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        # POST /accounts/:id
        # pk == id인 유저 조회, 직렬화
        user = self.get_object()
        data = UserSerializer(user).data

        # 해당 유정의 프로필 정보 조회
        # 존재하지 않는다면 공백
        profile = None
        try:
            if user.is_student:
                profile = StudentProfileSerializer(
                    StudentProfile.objects.get(user=user)).data
            elif user.is_carer:
                profile = CarerProfileSerializer(
                    CarerProfile.objects.get(user=user)).data
        finally:
            data['profile'] = profile or {}

        return Response(data=data)

    def create(self, request):
        user = request.user
        data = request.data
        query_params = request.query_params

        if user.is_student or user.is_carer:
            return Response({'detail': 'This user is already registered.'}, status=status.HTTP_400_BAD_REQUEST)

        if query_params.get('type') == 'student':
            profile_seriailzer = StudentProfileSerializer(data=data)
        elif query_params.get('type') == 'carer':
            profile_seriailzer = CarerProfileSerializer(data=data)
        else:
            return Response({"detail": "User type not passed."}, status=status.HTTP_400_BAD_REQUEST)

        if not profile_seriailzer.is_valid():
            return Response(profile_seriailzer.errors, status=status.HTTP_400_BAD_REQUEST)
        profile_seriailzer.save(user=user)
        user.set_type(query_params.get('type'))
        user.set_regist()

        data = UserSerializer(user).data
        data['profile'] = profile_seriailzer.data
        return Response(data=data)

    @action(detail=True, methods=['GET'])
    def rental(self, request, *args, **kwargs):
        user = self.get_object()
        rental_contracts = RentalContract.objects.filter(borrower=user)
        serializer = RentalContractSerializer(rental_contracts, many=True)
        return Response(serializer.data)
