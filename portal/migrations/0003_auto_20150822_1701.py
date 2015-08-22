# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_auto_20150821_0128'),
    ]

    operations = [
        migrations.CreateModel(
            name='illness',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('patientEmail', models.EmailField(max_length=30)),
                ('doctorEmail', models.EmailField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('emailId', models.EmailField(unique=True, max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('illness', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='displayName',
        ),
        migrations.AddField(
            model_name='doctor',
            name='patients',
            field=models.CharField(default='None', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='speciality',
            field=models.CharField(default='None', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctor',
            name='emailId',
            field=models.EmailField(unique=True, max_length=30),
        ),
    ]
