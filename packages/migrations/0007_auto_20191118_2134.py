# Generated by Django 2.2.6 on 2019-11-18 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0006_auto_20191118_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='passport',
            field=models.CharField(default='3213', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='visa',
            field=models.CharField(default='321312', max_length=100),
            preserve_default=False,
        ),
    ]
