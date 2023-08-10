from django.db import models
from django.contrib.auth import get_user_model


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


class RentalContract(models.Model):
    borrower = models.ForeignKey(
        to=get_user_model(), related_name="rental_contract", on_delete=models.CASCADE)
    rental = models.ForeignKey(
        to=Rental, related_name='rental_contract', on_delete=models.CASCADE)

    subscribe_date = models.DateField(auto_now_add=True)
    rental_start_at = models.DateField()
    rental_end_at = models.DateField()

    addressee_name = models.CharField(max_length=256)
    addressee_phone = models.CharField(max_length=64)
    address = models.CharField(max_length=256)
