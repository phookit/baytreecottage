# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('name', models.CharField(max_length=1024)),
                ('email', models.EmailField(max_length=254, blank=True, null=True)),
                ('tel', models.CharField(max_length=32)),
                ('info', models.TextField(max_length=1024, blank=True, null=True)),
                ('status', models.CharField(max_length=20, default='Reserved', choices=[('Available', 'Available'), ('Reserved', 'Reserved'), ('Booked', 'Booked')])),
            ],
            options={
                'ordering': ('start',),
            },
        ),
        migrations.CreateModel(
            name='BookingPrice',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('price', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ('start',),
            },
        ),
    ]
