# Generated by Django 3.0.8 on 2021-08-14 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAnimations', '0024_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='publish',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
