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
            name='MapLocal',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, serialize=False, parent_link=True, to='pages.Page', primary_key=True)),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Map And Local',
                'verbose_name_plural': 'Map and locals',
                'ordering': ('_order',),
            },
            bases=('pages.page', models.Model),
        ),
    ]
