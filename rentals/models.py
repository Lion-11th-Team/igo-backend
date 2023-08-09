from django.db import models


class Rental(models.Model):
    manufacturer = models.CharField(max_length=256)
    # iPhone 14, Galaxy 22 처럼 일반 사람들이 아는 그 이름
    model_name = models.CharField(max_length=256)
    # SM-f711N 처럼 제조 등록 코드
    model_code = models.CharField(max_length=256)
    manufacturing_date = models.DateField()
    registration_date = models.DateField(auto_now_add=True)
    battery_capacity = models.IntegerField()
    memory_amount = models.IntegerField()
    is_active = models.BooleanField(default=True)
    point = models.IntegerField()
