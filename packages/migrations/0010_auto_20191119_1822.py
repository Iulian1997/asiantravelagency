# Generated by Django 2.2.6 on 2019-11-19 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0009_auto_20191118_2211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='numOfGuests',
        ),
        migrations.AddField(
            model_name='package',
            name='email',
            field=models.CharField(default='test@test.com', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='mobile',
            field=models.CharField(default='323213', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='name',
            field=models.CharField(default='Test Test', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='numberOfGuests',
            field=models.CharField(default='2', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='package',
            name='breakfast',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='package',
            name='transport',
            field=models.BooleanField(default=False),
        ),
    ]
