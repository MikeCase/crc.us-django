# Generated by Django 5.0 on 2024-01-10 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bundle',
            name='products',
            field=models.ManyToManyField(related_name='bundles', to='website.product'),
        ),
    ]
