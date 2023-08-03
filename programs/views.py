from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

from programs.models import Program
from programs.serializers import ProgramSerializer
from .permissions import IsConsumerOrReadOnly


class ProgramViewSet(ModelViewSet):
    queryset = Program.objects.order_by('-created_at')
    serializer_class = ProgramSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsConsumerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=('POST', 'DELETE'))
    def subscribe(self, request, *args, **kwargs):
        # todo: 신청자 받아주는 조건 유효성 검사
        # 프로그램의 등록 상태, 등록 인원 등의 조건 검사 => 분기하여 처리
        program = self.get_object()
        
        if program.is_registing:
            current_time = timezone.now()
            if program.regist_start_at <= current_time <= program.regist_end_at:
                if request.method == 'POST':
                    program.subscriber.add(request.user)
                elif request.method == 'DELETE':
                    program.subscriber.remove(request.user)

                return Response(self.serializer_class(program).data)
            else:
                return Response({"message": "현재는 프로그램 모집 기간이 아닙니다."},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "현재는 프로그램 모집 기간이 아닙니다."},
                            status=status.HTTP_400_BAD_REQUEST)
