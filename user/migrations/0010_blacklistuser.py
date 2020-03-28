# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-03-28 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_user_can_review_blacklist'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlacklistUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email')),
                ('name', models.CharField(max_length=255, verbose_name='Full name')),
                ('justification', models.CharField(max_length=500)),
            ],
        ),
    ]
