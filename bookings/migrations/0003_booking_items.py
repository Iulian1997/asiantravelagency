# Generated by Django 2.2.6 on 2019-11-28 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0026_package_cost'),
        ('bookings', '0002_booking_ref_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='items',
            field=models.ManyToManyField(to='packages.Package'),
        ),
    ]
