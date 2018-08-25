# Generated by Django 2.0.7 on 2018-08-23 16:57

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20180823_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=imagekit.models.fields.ProcessedImageField(default='avatar_imgs/default.jpg', upload_to='avatar_imgs/%y/%m/%d', verbose_name='头像'),
        ),
    ]