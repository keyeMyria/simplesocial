# Generated by Django 2.0.5 on 2018-07-09 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='user',
        ),
        migrations.DeleteModel(
            name='Activity',
        ),
    ]
