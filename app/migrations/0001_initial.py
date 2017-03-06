# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AndroidMetadata',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('locale', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'android_metadata',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fix',
            fields=[
                ('number', models.TextField(serialize=False, primary_key=True)),
                ('name', models.TextField(null=True, blank=True)),
                ('address', models.TextField(null=True, blank=True)),
                ('province', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'fix',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Movil',
            fields=[
                ('number', models.TextField(serialize=False, primary_key=True)),
                ('name', models.TextField(null=True, blank=True)),
                ('identification', models.TextField(null=True, blank=True)),
                ('address', models.TextField(null=True, blank=True)),
                ('province', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'movil',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SqliteStat1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('tbl', models.TextField(null=True, blank=True)),
                ('idx', models.TextField(null=True, blank=True)),
                ('stat', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'sqlite_stat1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('version', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'version',
                'managed': False,
            },
        ),
    ]
