# Generated by Django 2.2.6 on 2019-11-20 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0022_auto_20191120_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='checkIn',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='package',
            name='checkOut',
            field=models.DateField(),
        ),
    ]
