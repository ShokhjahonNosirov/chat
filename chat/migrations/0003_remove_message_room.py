# Generated by Django 3.2.5 on 2021-08-03 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_message_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='room',
        ),
    ]