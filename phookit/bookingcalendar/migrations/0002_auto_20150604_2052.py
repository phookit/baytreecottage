# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookingcalendar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(max_length=20, choices=[('Available', 'Available'), ('Reserved', 'Reserved'), ('Booked', 'Booked'), ('Cancelled', 'Cancelled')], default='Reserved'),
        ),
    ]
