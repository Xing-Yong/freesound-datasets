# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-30 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0046_vote_from_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxonomynode',
            name='beginner_task',
            field=models.BooleanField(default=False),
        ),
    ]