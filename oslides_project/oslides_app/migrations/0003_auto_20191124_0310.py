# Generated by Django 2.2.7 on 2019-11-24 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oslides_app', '0002_auto_20191123_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.ImageField(upload_to='temp_images/'),
        ),
    ]
