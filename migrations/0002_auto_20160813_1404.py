# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time2eat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('country', models.CharField(max_length=10)),
                ('ResType', models.CharField(max_length=10)),
            ],
        ),
        migrations.RenameField(
            model_name='resprof',
            old_name='ResOpeningHr',
            new_name='last_reserv',
        ),
        migrations.RemoveField(
            model_name='resprof',
            name='ResLoc',
        ),
        migrations.RemoveField(
            model_name='resprof',
            name='ResName',
        ),
        migrations.RemoveField(
            model_name='resprof',
            name='ResPhone',
        ),
        migrations.AddField(
            model_name='resprof',
            name='address',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='resprof',
            name='district',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='resprof',
            name='phone',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AddField(
            model_name='resprof',
            name='restaurant',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='resprof',
            name='score',
            field=models.DecimalField(decimal_places=0, default=3, max_digits=1),
        ),
        migrations.AddField(
            model_name='resprof',
            name='service_h',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='resprof',
            name='ResType',
            field=models.ManyToManyField(to='time2eat.Type'),
        ),
    ]
