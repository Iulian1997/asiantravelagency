# Generated by Django 2.2.6 on 2019-12-03 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0016_auto_20191203_2157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='destination1',
        ),
        migrations.AddField(
            model_name='booking',
            name='destination',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
    ]