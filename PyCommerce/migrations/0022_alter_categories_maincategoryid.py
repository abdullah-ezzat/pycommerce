# Generated by Django 4.2.4 on 2023-08-13 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PyCommerce', '0021_alter_categories_maincategoryid_alter_orders_cartid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='MainCategoryId',
            field=models.ForeignKey(db_column='MainCategoryId', db_constraint=False, default='null', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.categories'),
        ),
    ]
