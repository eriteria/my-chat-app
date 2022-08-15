# Generated by Django 4.0.5 on 2022-07-12 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('room', '0005_remove_room_members_room_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_rooms', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='members',
            field=models.ManyToManyField(default=None, related_name='rooms', to=settings.AUTH_USER_MODEL),
        ),
    ]
