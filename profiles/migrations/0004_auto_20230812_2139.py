# Generated by Django 3.2.20 on 2023-08-12 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20230812_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carerprofile',
            name='image',
            field=models.ImageField(default='default_profile.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='image',
            field=models.ImageField(default='default_profile.png', upload_to=''),
        ),
    ]
