# Generated by Django 5.0.7 on 2024-07-31 07:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('cat_img', models.ImageField(upload_to='category_img')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('date_createtime', models.DateField(auto_now_add=True)),
                ('date_updatetime', models.DateField(auto_now=True)),
                ('image', models.ImageField(upload_to='Prodect_img')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Watches.brand_name')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Watches.category')),
            ],
        ),
    ]