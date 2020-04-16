# Generated by Django 3.0.4 on 2020-04-16 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_postcode_location'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postcode',
            options={'ordering': ['postcode']},
        ),
        migrations.AlterField(
            model_name='postcode',
            name='postcode',
            field=models.PositiveSmallIntegerField(unique=True),
        ),
    ]