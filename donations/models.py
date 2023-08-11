from django.db import models

DONATION_MODEL_CATEGORY = (
    ('smartphone', '스마트폰'),
    ('tablet', '태블릿'),
    ('laptop', '노트북'),
)

class Donation(models.Model):
    model_category = models.CharField(max_length=20, choices=DONATION_MODEL_CATEGORY)
    model_name = models.CharField(max_length=256)
    remarks = models.CharField(max_length=256)

    sender_name = models.CharField(max_length=256)
    sender_phone = models.CharField(max_length=64)
    sender_address = models.CharField(max_length=256)
    content = models.CharField(max_length=256)
