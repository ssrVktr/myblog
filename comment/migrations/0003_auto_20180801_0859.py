# Generated by Django 2.0.7 on 2018-08-01 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20180729_1502'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['comment_time']},
        ),
    ]
