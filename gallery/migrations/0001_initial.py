# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('artist', models.CharField(max_length=120, blank=True)),
                ('title', models.CharField(max_length=120, blank=True)),
                ('url', models.CharField(max_length=400, blank=True)),
                ('size', models.CharField(max_length=120, blank=True)),
                ('medium', models.CharField(max_length=120, blank=True)),
                ('price', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
