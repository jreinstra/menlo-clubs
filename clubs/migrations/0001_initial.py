# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('short_description', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('meeting_day', models.IntegerField(default=(0, b'Monday'), choices=[(0, b'Monday'), (1, b'Tuesday'), (2, b'Wednesday'), (3, b'Thursday'), (4, b'Friday'), (5, b'Saturday'), (6, b'Sunday')])),
                ('meeting_time', models.TimeField()),
                ('meeting_location', models.CharField(max_length=50)),
                ('contact_email', models.CharField(max_length=200)),
            ],
        ),
    ]
