# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookingcalendar', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calendaritem',
            old_name='end_day',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='calendaritem',
            old_name='start_day',
            new_name='start',
        ),
    ]
