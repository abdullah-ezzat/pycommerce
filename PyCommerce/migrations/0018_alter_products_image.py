# Generated by Django 3.2.5 on 2021-08-02 12:47

import PyCommerce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PyCommerce', '0017_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]