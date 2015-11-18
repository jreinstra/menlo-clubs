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
            name='student_leaders',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='club',
            name='teacher_leaders',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='club',
            name='contact_email',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
