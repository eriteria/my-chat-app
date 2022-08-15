# Generated by Django 4.0.5 on 2022-07-12 16:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('room', '0004_room_members_alter_room_visibility'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='members',
        ),
        migrations.AddField(
            model_name='room',
            name='members',
            field=models.ManyToManyField(related_name='rooms', to=settings.AUTH_USER_MODEL),
        ),
    ]