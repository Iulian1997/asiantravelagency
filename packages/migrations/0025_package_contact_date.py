# Generated by Django 2.2.6 on 2019-11-20 23:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0024_package_destination_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='contact_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
