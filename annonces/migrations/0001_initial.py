# Generated by Django 4.1.4 on 2022-12-30 13:34

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('regions', '0001_initial'),
    ]

    operations = [
        
        migrations.CreateModel(
            name='TypeAnnonce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BienImmobilier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photos', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10000), size=None)),
                ('commune', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regions.commune')),
                ('wilaya', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regions.wilaya')),
            ],
        ),
        migrations.CreateModel(
            name='Annonce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=3000)),
                ('bienImmobilier', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='annonces.bienimmobilier')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annonces.typeannonce')),
            ],
        ),
    ]
