# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=taggit.managers.TaggableManager(verbose_name='Tags', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', to='taggit.Tag'),
        ),
    ]
