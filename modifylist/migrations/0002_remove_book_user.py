# Generated by Django 2.0.6 on 2018-11-27 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modifylist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='user',
        ),
    ]