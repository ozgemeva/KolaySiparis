# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-10 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KolaySiparisApp', '0003_auto_20151210_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='totalprice',
            field=models.IntegerField(default=0),
        ),
    ]