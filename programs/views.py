from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

from programs.models import Program
from programs.serializers import ProgramSerializer
from .permissions import IsCarerOrReadOnly, IsStudent


class ProgramViewSet(ModelViewSet):
    queryset = Program.objects.order_by('-created_at')
    serializer_class = ProgramSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsCarerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def get_permissions(self):
        if self.action == 'subscribe':
            self.permission_classes = [IsStudent]
        return super().get_permissions()


    @action(detail=True, methods=('POST', 'DELETE'))
    def subscribe(self, request, *args, **kwargs):
        # todo: 신청자 받아주는 조건 유효성 검사
        # 프로그램의 등록 상태, 등록 인원 등의 조건 검사 => 분기하여 처리
        program = self.get_object()
        
        if program.is_registing: # 프로그램이 모집 여부 고려
            current_time = timezone.now()
            if program.regist_start_at <= current_time <= program.regist_end_at: # 프로그램의 기간 고려
                if program.subscriber_num < program.subscriber_limit: # 프로그램 정원 수 고려
                    if request.method == 'POST':
                        program.subscriber.add(request.user)
                        program.subscriber_num += 1
                        if program.subscriber_num == program.subscriber_limit:
                            program.is_registing = False
                        program.save()
                        return Response(self.serializer_class(program).data)
                    elif request.method == 'DELETE':
                        program.subscriber.remove(request.user)
                        program.subscriber_num -= 1
                        program.save()
                        return Response(self.serializer_class(program).data)
                else:
                    return Response({"message": "현재는 프로그램 인원이 마감되었습니다."},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"message": "현재는 프로그램 모집 기간이 아닙니다."},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "현재는 프로그램 모집 기간이 아닙니다."},
                            status=status.HTTP_400_BAD_REQUEST)
