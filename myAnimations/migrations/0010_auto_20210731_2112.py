# Generated by Django 3.2.5 on 2021-07-31 15:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAnimations', '0009_remove_myanimations_animation_createdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='myanimations',
            name='animation_createdate',
            field=models.DateTimeField(default=datetime.datetime.now, null=True, verbose_name='date created at'),
        ),
        migrations.AlterField(
            model_name='myanimations',
            name='animation_details',
            field=models.TextField(max_length=500),
        ),
    ]
