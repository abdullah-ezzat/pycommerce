# Generated by Django 3.2.5 on 2021-07-25 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PyCommerce', '0010_alter_products_image4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='ImageUrl',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
