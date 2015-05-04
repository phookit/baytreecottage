# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20141227_0224'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacilitiesPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, to='pages.Page', auto_created=True, primary_key=True, parent_link=True)),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Facilities page',
                'verbose_name_plural': 'Facilities pages',
                'ordering': ('_order',),
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('_order', mezzanine.core.fields.OrderField(verbose_name='Order', null=True)),
                ('title', models.CharField(max_length=64)),
                ('filename', models.FileField(upload_to='facilityimages')),
                ('description', models.CharField(null=True, blank=True, max_length=512)),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('_order', mezzanine.core.fields.OrderField(verbose_name='Order', null=True)),
                ('title', models.CharField(max_length=64)),
                ('facilitiespage', models.ForeignKey(to='facilities.FacilitiesPage', related_name='sections')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.AddField(
            model_name='image',
            name='section',
            field=models.ForeignKey(to='facilities.Section', related_name='images'),
        ),
    ]
