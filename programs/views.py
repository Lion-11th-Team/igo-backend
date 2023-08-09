from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

from programs.models import Program
from programs.serializers import ProgramSerializer
from .permissions import IsCarer, IsProgramAuthor, IsStudent


class ProgramViewSet(ModelViewSet):
    queryset = Program.objects.order_by('-created_at')
    serializer_class = ProgramSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action == 'subscribe':
            permission_classes = [IsAuthenticated, IsStudent]
        elif self.action in ['create']:
            permission_classes = [IsAuthenticated, IsCarer]
        elif self.action in ['update', 'partial_update', 'delete']:
            permission_classes = [IsAuthenticated, IsCarer, IsProgramAuthor]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(detail=True, methods=('POST', 'DELETE'))
    def subscribe(self, request, *args, **kwargs):
        program = self.get_object()

        if program.is_registing:
            if request.method == 'POST':
                program.subscriber.add(request.user)
                program.subscriber_num += 1
                program.save()
                return Response(self.serializer_class(program).data)
            elif request.method == 'DELETE':
                program.subscriber.remove(request.user)
                program.subscriber_num -= 1
                program.save()
                return Response(self.serializer_class(program).data)
        else:
            return Response({"detail": "현재는 프로그램 모집 기간이 아닙니다."},
                            status=status.HTTP_400_BAD_REQUEST)
