# Generated by Django 4.1.4 on 2023-01-06 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annonces', '0004_contact_annonce_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='annonce',
            name='date',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
