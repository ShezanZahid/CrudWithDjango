# Generated by Django 3.2.5 on 2021-07-31 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAnimations', '0016_myanimations_animation_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myanimations',
            name='animation_image',
            field=models.ImageField(default='images/None/Noimg.jpg', upload_to='images/'),
        ),
    ]
