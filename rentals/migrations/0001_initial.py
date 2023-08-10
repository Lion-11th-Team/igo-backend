# Generated by Django 3.2.20 on 2023-08-10 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=256)),
                ('model_name', models.CharField(max_length=256)),
                ('model_code', models.CharField(max_length=256)),
                ('manufacturing_date', models.DateField()),
                ('registration_date', models.DateField(auto_now_add=True)),
                ('battery_capacity', models.IntegerField()),
                ('memory_amount', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('rental_start_at', models.DateField()),
                ('rental_end_at', models.DateField()),
                ('point', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RentalContract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribe_date', models.DateField(auto_now_add=True)),
                ('rental_start_at', models.DateField()),
                ('rental_end_at', models.DateField()),
                ('addressee_name', models.CharField(max_length=256)),
                ('addressee_phone', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=256)),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rental_contract', to=settings.AUTH_USER_MODEL)),
                ('rental', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rental_contract', to='rentals.rental')),
            ],
        ),
    ]
