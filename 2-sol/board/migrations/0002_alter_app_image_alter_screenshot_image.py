# Generated by Django 4.1.7 on 2023-03-14 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='image',
            field=models.ImageField(upload_to='media/app_images/'),
        ),
        migrations.AlterField(
            model_name='screenshot',
            name='image',
            field=models.ImageField(upload_to='media/task_screenshots/'),
        ),
    ]
