# Generated by Django 2.2.17 on 2021-04-04 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matemaker', '0007_auto_20210404_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interest',
            name='slug',
        ),
    ]
