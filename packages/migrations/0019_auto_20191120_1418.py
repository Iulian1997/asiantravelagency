# Generated by Django 2.2.6 on 2019-11-20 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0018_auto_20191120_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='checkIn',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='package',
            name='checkOut',
            field=models.CharField(max_length=200),
        ),
    ]
