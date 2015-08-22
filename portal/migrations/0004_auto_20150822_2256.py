# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20150822_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='allergie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=30)),
                ('allergies', models.TextField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last', models.DateField(max_length=30)),
                ('next', models.DateField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='diagnosis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ailment', models.CharField(max_length=30)),
                ('doctorName', models.CharField(max_length=30)),
                ('doctorEmail', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='onlineConsultation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last', models.DateField(max_length=30)),
                ('next', models.DateField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.IntegerField(max_length=10)),
                ('age', models.CharField(max_length=3)),
                ('phone', models.IntegerField(max_length=15)),
                ('address', models.TextField(max_length=60)),
            ],
        ),
        migrations.DeleteModel(
            name='illness',
        ),
    ]
