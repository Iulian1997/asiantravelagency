# Generated by Django 2.2.6 on 2019-11-18 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0002_auto_20191024_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='address',
        ),
        migrations.RemoveField(
            model_name='package',
            name='email',
        ),
        migrations.RemoveField(
            model_name='package',
            name='name',
        ),
        migrations.RemoveField(
            model_name='package',
            name='number',
        ),
        migrations.RemoveField(
            model_name='package',
            name='zipcode',
        ),
    ]