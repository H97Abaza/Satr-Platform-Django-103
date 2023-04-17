# Generated by Django 4.2 on 2023-04-17 12:07

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=254)),
                ('profile', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='seller/photos/')),
            ],
            options={
                'verbose_name': 'Seller',
                'verbose_name_plural': 'Sellers',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('photo', models.ImageField(upload_to='products/photos/')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.seller')),
            ],
            options={
                'verbose_name': 'Products',
                'verbose_name_plural': 'Productss',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
