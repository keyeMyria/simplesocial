# Generated by Django 2.0.5 on 2018-07-21 09:44

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofileinfo_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='weight',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
    ]
