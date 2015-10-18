# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0019_verbose_names_cleanup'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='wsgi_port',
            field=models.IntegerField(help_text='The port that is configured in nginx configuration for the site.', verbose_name='Port', default=80),
        ),
    ]
