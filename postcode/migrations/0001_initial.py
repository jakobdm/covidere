# Generated by Django 3.0.5 on 2020-04-22 06:51

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postcode', models.PositiveSmallIntegerField(unique=True)),
                ('city', models.CharField(max_length=100)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['postcode'],
            },
        ),
    ]
