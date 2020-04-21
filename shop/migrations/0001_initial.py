# Generated by Django 3.0.4 on 2020-04-21 11:29

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('postcode', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='shop name')),
                ('address', models.CharField(max_length=100, verbose_name='address')),
                ('homepage', models.URLField(verbose_name='homepage')),
                ('email', models.EmailField(max_length=254, verbose_name='contact email')),
                ('phone', models.CharField(max_length=20, verbose_name='phone')),
                ('active', models.BooleanField(default=False, verbose_name='active')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('delivery_postcode', models.ManyToManyField(blank=True, to='postcode.Postcode')),
                ('postcode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shops', to='postcode.Postcode')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
