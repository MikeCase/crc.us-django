# Generated by Django 5.0 on 2024-01-11 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_alter_bundle_products'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bundle',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
