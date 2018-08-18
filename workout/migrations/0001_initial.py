# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-09 09:58
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise', models.TextField()),
                ('order', models.IntegerField(blank=True, null=True)),
                ('sets', models.IntegerField(default=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('reps', models.IntegerField(choices=[(0, 'Kilometers'), (1, 'Reps')], default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(600)])),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation date', models.DateField(auto_now_add=True)),
                ('day', models.CharField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], max_length=1)),
                ('title', models.CharField(max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workout', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='set',
            name='workout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workout.Workout'),
        ),
    ]