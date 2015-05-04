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
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, parent_link=True, auto_created=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('change_over_day', models.CharField(max_length=32)),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name_plural': 'Home Pages',
                'verbose_name': 'Home Page',
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('_order', mezzanine.core.fields.OrderField(verbose_name='Order', null=True)),
                ('image', mezzanine.core.fields.FileField(max_length=255, null=True, blank=True, verbose_name='Image')),
                ('caption', models.CharField(max_length=64, null=True, blank=True)),
                ('text_colour', models.CharField(default='#ffffff', max_length=15, null=True, blank=True, verbose_name='Text Colour')),
                ('homepage', models.ForeignKey(related_name='slides', to='baytreecottage.HomePage')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('_order', mezzanine.core.fields.OrderField(verbose_name='Order', null=True)),
                ('title', models.CharField(max_length=200, null=True, blank=True)),
                ('image', mezzanine.core.fields.FileField(max_length=255, null=True, blank=True, verbose_name='Image')),
                ('image_align', models.CharField(default='left', max_length=5, choices=[('left', 'Left'), ('right', 'Right')])),
                ('homepage', models.ForeignKey(related_name='statements', to='baytreecottage.HomePage')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
    ]
