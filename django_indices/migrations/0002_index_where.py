# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-08-06 06:17
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("django_indices", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="index",
            name="where",
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        )
    ]
