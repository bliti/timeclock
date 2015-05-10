# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.TextField()),
                ('name', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('organization', models.ForeignKey(to='organizations.Organization')),
            ],
        ),
    ]
