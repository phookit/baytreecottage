# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarItem',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('start_day', models.DateField()),
                ('end_day', models.DateField()),
                ('title', models.CharField(max_length=128)),
                ('url', models.URLField(null=True, blank=True)),
                ('status', models.CharField(max_length=20, choices=[('Available', 'Available'), ('Reserved', 'Reserved'), ('Booked', 'Booked')], default='Available')),
            ],
        ),
    ]
