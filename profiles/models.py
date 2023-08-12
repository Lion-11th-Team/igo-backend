from django.contrib.auth import get_user_model
from django.db import models


class StudentProfile(models.Model):
    user = models.ForeignKey(
        to=get_user_model(), related_name='student_profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    image = models.ImageField(default='default_profile.png')
    birthdate = models.DateField()
    phone = models.CharField(max_length=64)
    email = models.CharField(max_length=256)
    # location = models.


class CarerProfile(models.Model):
    user = models.ForeignKey(
        to=get_user_model(), related_name='carer_profile', on_delete=models.CASCADE)
    facility_name = models.CharField(max_length=256)
    admin_name = models.CharField(max_length=256)
    image = models.ImageField(default='default_profile.png')
    phone = models.CharField(max_length=64)
    email = models.CharField(max_length=256)
    # location = models.
