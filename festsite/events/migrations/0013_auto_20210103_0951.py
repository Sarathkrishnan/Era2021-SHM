# Generated by Django 3.1.4 on 2021-01-03 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_events_event_banner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='isGroup',
            new_name='is_Group',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='maxNoOfGroupMembers',
            new_name='max_GroupMembers',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='minNoOfGroupMembers',
            new_name='min_GroupMembers',
        ),
    ]