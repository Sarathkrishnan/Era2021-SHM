# Generated by Django 3.1.5 on 2021-01-06 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0004_eventregistration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregistration',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='festevent',
            name='name',
            field=models.CharField(max_length=55),
        ),
    ]