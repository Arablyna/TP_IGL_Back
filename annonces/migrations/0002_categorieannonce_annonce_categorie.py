# Generated by Django 4.1.4 on 2023-01-05 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('annonces', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategorieAnnonce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='annonce',
            name='categorie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='annonces.categorieannonce'),
            preserve_default=False,
        ),
    ]
