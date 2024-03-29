# Generated by Django 2.2.6 on 2019-11-18 20:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0003_auto_20191118_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='address',
            field=models.CharField(default=12, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='email',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='name',
            field=models.CharField(default='12 Dog', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='number',
            field=models.CharField(default=321321, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='zipcode',
            field=models.CharField(default='test', max_length=20),
            preserve_default=False,
        ),
    ]
