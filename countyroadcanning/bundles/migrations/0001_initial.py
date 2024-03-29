# Generated by Django 5.0 on 2024-01-11 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bundle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('description', models.CharField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('products', models.ManyToManyField(related_name='bundles', to='products.product')),
            ],
        ),
    ]
