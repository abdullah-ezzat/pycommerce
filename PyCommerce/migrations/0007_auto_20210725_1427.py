# Generated by Django 3.2.5 on 2021-07-25 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PyCommerce', '0006_gethomeproducts_specificationvaluecount_starpercent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brands',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='products',
            name='Image4',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
