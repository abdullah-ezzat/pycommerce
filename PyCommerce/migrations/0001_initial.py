# Generated by Django 3.2.5 on 2021-07-08 17:55

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='brands',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('NameA', models.TextField(max_length=2550, null=True)),
                ('NameL', models.TextField(max_length=2550)),
            ],
        ),
        migrations.CreateModel(
            name='cartTransactionMasters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateCreated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='cartTransactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.FloatField()),
                ('IsOrdered', models.IntegerField()),
                ('MasterId', models.ForeignKey(db_column='MasterId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.carttransactionmasters')),
            ],
        ),
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameA', models.TextField(max_length=2550, null=True)),
                ('NameL', models.TextField(max_length=2550)),
                ('Level', models.IntegerField()),
                ('ImageUrl', models.TextField(max_length=2550, null=True)),
                ('MainCategoryId', models.ForeignKey(db_column='MainCategoryId', db_constraint=False, default='null', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.categories')),
            ],
        ),
        migrations.CreateModel(
            name='countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameA', models.TextField(max_length=2550, null=True)),
                ('NameL', models.TextField(max_length=2550)),
                ('Symbol', models.TextField(max_length=2550)),
            ],
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UnitPrice', models.FloatField()),
                ('TotalPrice', models.FloatField()),
                ('isDelivered', models.BooleanField()),
                ('Latitude', models.TextField(max_length=2550, null=True)),
                ('Longitude', models.TextField(max_length=2550, null=True)),
                ('Quantity', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='orderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.IntegerField()),
                ('StatusNameA', models.TextField(max_length=2550, null=True)),
                ('StatusNameL', models.TextField(max_length=2550)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameA', models.TextField(max_length=2550, null=True)),
                ('NameL', models.TextField(max_length=2550)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='')),
                ('Image2', models.ImageField(blank=True, null=True, upload_to='')),
                ('Image3', models.ImageField(blank=True, null=True, upload_to='')),
                ('Image4', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('Description', models.TextField(max_length=2550, null=True)),
                ('BrandId', models.ForeignKey(db_column='BrandId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.brands')),
                ('CategoryId', models.ForeignKey(db_column='CategoryId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.categories')),
            ],
        ),
        migrations.CreateModel(
            name='shippingAgents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameA', models.TextField(max_length=2550, null=True)),
                ('NameL', models.TextField(max_length=2550)),
                ('Address1', models.TextField(max_length=2550)),
                ('Address2', models.TextField(max_length=2550, null=True)),
                ('Phone', models.TextField(max_length=2550, null=True)),
                ('Email', models.TextField(max_length=2550)),
                ('Password', models.TextField(max_length=2550)),
                ('PostCode', models.TextField(max_length=2550, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='specifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameA', models.TextField(max_length=2550, null=True)),
                ('NameL', models.TextField(max_length=2550)),
                ('ShowInFilter', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='specificationValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=2550)),
            ],
        ),
        migrations.CreateModel(
            name='stores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameA', models.TextField(max_length=2550, null=True)),
                ('NameL', models.TextField(max_length=2550)),
                ('Email', models.TextField(max_length=2550)),
                ('Address', models.TextField(max_length=2550, null=True)),
                ('City', models.TextField(max_length=2550)),
                ('Latitude', models.TextField(max_length=2550, null=True)),
                ('Longitude', models.TextField(max_length=2550, null=True)),
                ('CountryId', models.ForeignKey(db_column='CountryId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.countries')),
                ('ShippingAgentId', models.ForeignKey(db_column='ShippingAgentId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.shippingagents')),
            ],
        ),
        migrations.CreateModel(
            name='transactionTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.IntegerField()),
                ('NameA', models.TextField(max_length=2550, null=True)),
                ('NameL', models.TextField(max_length=2550)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameA', models.TextField(max_length=2550, null=True)),
                ('NameL', models.TextField(max_length=2550)),
                ('Email', models.TextField(max_length=2550)),
                ('Password', models.TextField(max_length=2550)),
                ('Address1', models.TextField(max_length=2550, null=True)),
                ('Address2', models.TextField(max_length=2550, null=True)),
                ('Phone', models.IntegerField(null=True)),
                ('City', models.TextField(max_length=2550, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='vendors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameA', models.TextField(max_length=2550, null=True)),
                ('NameL', models.TextField(max_length=2550)),
                ('Address1', models.TextField(max_length=2550)),
                ('Address2', models.TextField(max_length=2550, null=True)),
                ('Phone', models.TextField(max_length=2550, null=True)),
                ('Email', models.TextField(max_length=2550)),
                ('Password', models.TextField(max_length=2550)),
                ('PostCode', models.TextField(max_length=2550, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='vendorPriceLists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.FloatField()),
                ('CountryId', models.ForeignKey(db_column='CountryId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.countries')),
                ('ProductId', models.ForeignKey(db_column='ProductId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.products')),
                ('VendorId', models.ForeignKey(db_column='VendorId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.vendors')),
            ],
        ),
        migrations.CreateModel(
            name='storeShippingAgents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShippingAgentId', models.ForeignKey(db_column='ShippingAgentId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.shippingagents')),
                ('StoreId', models.ForeignKey(db_column='StoreId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.stores')),
            ],
        ),
        migrations.AddField(
            model_name='stores',
            name='VendorId',
            field=models.ForeignKey(db_column='VendorId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.vendors'),
        ),
        migrations.CreateModel(
            name='shippingDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DeliveryNotes', models.TextField(max_length=2550, null=True)),
                ('OrderId', models.ForeignKey(db_column='OrderId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.orders')),
                ('ShippingAgentId', models.ForeignKey(db_column='ShippingAgentId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.shippingagents')),
            ],
        ),
        migrations.CreateModel(
            name='shippingAgentUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShippingAgentId', models.ForeignKey(db_column='ShippingAgentId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.shippingagents')),
                ('UserId', models.ForeignKey(db_column='UserId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.users')),
            ],
        ),
        migrations.CreateModel(
            name='productStoreRatings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RatingId', models.IntegerField()),
                ('ProductReview', models.TextField(max_length=2550, null=True)),
                ('ProductId', models.ForeignKey(db_column='ProductId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.products')),
                ('StoreId', models.ForeignKey(db_column='StoreId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.stores')),
                ('UserId', models.ForeignKey(db_column='UserId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.users')),
            ],
        ),
        migrations.CreateModel(
            name='productSpecifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SpecificationName', models.TextField(max_length=2550)),
                ('SpecificationValue', models.TextField(max_length=2550)),
                ('ShowInFilter', models.BooleanField(null=True)),
                ('CategoryId', models.ForeignKey(db_column='CategoryId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.categories')),
                ('ProductId', models.ForeignKey(db_column='ProductId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.products')),
                ('SpecificationId', models.ForeignKey(db_column='SpecificationId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.specifications')),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='DeliveredByUserId',
            field=models.ForeignKey(db_column='DeliveredByUserId', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='UserId', to='PyCommerce.users'),
        ),
        migrations.AddField(
            model_name='orders',
            name='MasterId',
            field=models.ForeignKey(db_column='MasterId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.carttransactionmasters'),
        ),
        migrations.AddField(
            model_name='orders',
            name='ProductId',
            field=models.ForeignKey(db_column='ProductId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.products'),
        ),
        migrations.AddField(
            model_name='orders',
            name='ShippingAgentId',
            field=models.ForeignKey(db_column='ShippingAgentId', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.shippingagents'),
        ),
        migrations.AddField(
            model_name='orders',
            name='StoreId',
            field=models.ForeignKey(db_column='StoreId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.stores'),
        ),
        migrations.AddField(
            model_name='orders',
            name='UserId',
            field=models.ForeignKey(db_column='UserId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.users'),
        ),
        migrations.AddField(
            model_name='orders',
            name='cartId',
            field=models.ForeignKey(db_column='CartId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.carttransactions'),
        ),
        migrations.CreateModel(
            name='orderMasters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateCreated', models.DateTimeField()),
                ('ShippingAddress', models.TextField(max_length=2550, null=True)),
                ('OrderStatusId', models.ForeignKey(db_column='OrderStatusId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.orderstatus')),
                ('UserId', models.ForeignKey(db_column='UserId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.users')),
                ('cartId', models.ForeignKey(db_column='CartId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.carttransactions')),
            ],
        ),
        migrations.CreateModel(
            name='inventoryDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.FloatField()),
                ('ProductId', models.ForeignKey(db_column='ProductId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.products')),
                ('StoreId', models.ForeignKey(db_column='StoreId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.stores')),
            ],
        ),
        migrations.CreateModel(
            name='inventoryBalances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QuantityBalance', models.FloatField()),
                ('ProductId', models.ForeignKey(db_column='ProductId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.products')),
                ('StoreId', models.ForeignKey(db_column='StoreId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.stores')),
            ],
        ),
        migrations.AddField(
            model_name='carttransactions',
            name='ProductId',
            field=models.ForeignKey(db_column='ProductId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.products'),
        ),
        migrations.AddField(
            model_name='carttransactions',
            name='StoreId',
            field=models.ForeignKey(db_column='StoreId', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='PyCommerce.stores'),
        ),
    ]
