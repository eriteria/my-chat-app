# Generated by Django 4.0.5 on 2022-07-12 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('room', '0003_room_visibility'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='members',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='rooms', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='visibility',
            field=models.CharField(choices=[('1', 'public'), ('2', 'private')], default='public', max_length=10),
        ),
    ]
