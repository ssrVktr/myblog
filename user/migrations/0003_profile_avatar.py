# Generated by Django 2.0.7 on 2018-08-23 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20180804_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='avatar_imgs/default.jpg', height_field='100', upload_to='avatar_imgs/%y/%m/%d', verbose_name='头像', width_field='100'),
        ),
    ]
