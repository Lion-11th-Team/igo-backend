from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from accounts.serializer import UserSerializer
from profiles.serializers import CarerProfileSerializer, StudentProfileSerializer

User = get_user_model()


class AccountsInfo(APIView):
    allowed_methods = ('GET', 'POST')
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        # todo: GET /accounts/:pk -> user.pk == pk인 user -> data + user type의 profile
        return Response(UserSerializer(request.user).data)

    def post(self, request):
        user = request.user
        data = request.data
        query_params = request.query_params

        if query_params.get('type') == 'student':
            profile_seriailzer = StudentProfileSerializer(user, data=data)
        elif query_params.get('type') == 'carer':
            profile_seriailzer = CarerProfileSerializer(user, data=data)
        else:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

        if not profile_seriailzer.is_valid():
            return Response(profile_seriailzer.errors, status=status.HTTP_400_BAD_REQUEST)
        profile_seriailzer.save()

        profile_seriailzer.save(user=user)
        user.set_type(query_params.get('type'))
        user.set_regist()

        data = UserSerializer(user).data
        data['profile'] = profile_seriailzer.data
        return Response(data=data)
