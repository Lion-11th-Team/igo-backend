from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db import models


class Program(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(
        to=get_user_model(), related_name='author', on_delete=models.CASCADE)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    regist_start_at = models.DateTimeField()
    regist_end_at = models.DateTimeField()

    activity_start_at = models.DateTimeField()
    activity_end_at = models.DateTimeField()

    is_registing = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)

    subscriber_limit = models.IntegerField()
    subscriber_num = models.IntegerField(default=0)
    subscriber = models.ManyToManyField(
        to=get_user_model(), related_name='program')
    
    activity_field_choices = (
        ('kiosk', '키오스크'),
        ('app_payment', '앱 결제'),
        ('bank_transfer', '계좌 이체'),
        # 다른 분야도 추가 예정
    )

    activity_field = models.CharField(max_length=50, choices=activity_field_choices)
    area = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)
