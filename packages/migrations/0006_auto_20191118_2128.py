# Generated by Django 2.2.6 on 2019-11-18 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0005_auto_20191118_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='email',
            field=models.CharField(default='test@test.com', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='number',
            field=models.CharField(default='3213213', max_length=20),
            preserve_default=False,
        ),
    ]