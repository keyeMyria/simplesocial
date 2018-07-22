# Generated by Django 2.0.5 on 2018-07-21 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20180721_1317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weightlist',
            name='user_weight',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='body_fat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='height',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
