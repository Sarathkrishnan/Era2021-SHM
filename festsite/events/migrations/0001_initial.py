# Generated by Django 3.1.4 on 2021-01-01 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('decription', models.CharField(max_length=100)),
                ('fees', models.IntegerField()),
                ('contact', models.CharField(max_length=15)),
            ],
        ),
    ]