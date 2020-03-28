# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-03-16 16:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('applications', '0019_auto_20200210_0838'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='blacklisted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blacklisted_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='application',
            name='reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('P', 'Under review'), ('R', 'Wait listed'), ('I', 'Invited'), ('LR', 'Last reminder'), ('C', 'Confirmed'), ('X', 'Cancelled'), ('A', 'Attended'), ('E', 'Expired'), ('D', 'Dubious'), ('IV', 'Invalid'), ('BL', 'Black Listed')], default='P', max_length=2),
        ),
    ]
