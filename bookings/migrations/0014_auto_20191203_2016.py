# Generated by Django 2.2.6 on 2019-12-03 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0013_auto_20191203_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='destination',
        ),
        migrations.AddField(
            model_name='booking',
            name='destination',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
    ]