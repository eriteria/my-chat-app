# Generated by Django 4.0.5 on 2022-07-12 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='visibility',
            field=models.CharField(choices=[(1, 'public'), (2, 'private')], default='public', max_length=10),
        ),
    ]
