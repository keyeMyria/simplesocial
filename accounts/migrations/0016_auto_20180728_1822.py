# Generated by Django 2.0.5 on 2018-07-28 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_userprofileinfo_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weightlist',
            name='timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]