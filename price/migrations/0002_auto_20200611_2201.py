# Generated by Django 3.0.6 on 2020-06-11 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='finish',
        ),
    ]
