# Generated by Django 3.1.4 on 2021-01-03 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20210103_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='event_banner',
            field=models.ImageField(default=None, upload_to=None),
        ),
    ]