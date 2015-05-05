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
                ('page_ptr', models.OneToOneField(to='pages.Page', auto_created=True, parent_link=True, serialize=False, primary_key=True)),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('extra_info', mezzanine.core.fields.RichTextField(default='<p></p>')),
            ],
            options={
                'verbose_name': 'Map And Local',
                'verbose_name_plural': 'Map and locals',
                'ordering': ('_order',),
            },
            bases=('pages.page', models.Model),
        ),
    ]
