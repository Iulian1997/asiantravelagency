# Generated by Django 2.2.6 on 2019-11-18 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0007_auto_20191118_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='user_id',
            field=models.IntegerField(blank=True, default=12),
            preserve_default=False,
        ),
    ]
