# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='short_description',
            field=models.CharField(default='Needs desc', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='club',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
