# Generated by Django 2.2.6 on 2019-12-04 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_code', models.CharField(max_length=200)),
                ('user_id', models.IntegerField(blank=True)),
                ('is_ordered', models.BooleanField(default=False)),
                ('destination', models.CharField(max_length=200)),
                ('destination_id', models.IntegerField()),
                ('date_ordered', models.DateTimeField(auto_now=True)),
                ('cost', models.FloatField()),
            ],
        ),
    ]
