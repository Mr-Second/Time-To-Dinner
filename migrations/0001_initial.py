# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResProf',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('ResName', models.CharField(max_length=15)),
                ('ResLoc', models.CharField(max_length=30)),
                ('ResOpeningHr', models.CharField(max_length=20)),
                ('ResPhone', models.CharField(max_length=12)),
                ('ResLike', models.DecimalField(max_digits=6, decimal_places=0, default=50)),
                ('create', models.DateTimeField()),
            ],
        ),
    ]
