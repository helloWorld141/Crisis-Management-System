# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-07 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crisis', '0011_auto_20170408_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='userType',
            field=models.IntegerField(choices=[(1, 'Call Operator'), (2, 'Civil Defense'), (3, 'LTA'), (4, 'Police')], null=True),
        ),
    ]
