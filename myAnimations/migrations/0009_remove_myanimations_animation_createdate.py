# Generated by Django 3.2.5 on 2021-07-31 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myAnimations', '0008_alter_myanimations_animation_createdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myanimations',
            name='animation_createdate',
        ),
    ]
