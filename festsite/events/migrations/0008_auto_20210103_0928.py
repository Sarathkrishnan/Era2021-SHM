# Generated by Django 3.1.4 on 2021-01-03 09:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20210103_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='events',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
