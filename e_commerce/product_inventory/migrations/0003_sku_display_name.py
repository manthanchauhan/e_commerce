# Generated by Django 4.1.1 on 2022-09-11 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_inventory', '0002_alter_sku_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='sku',
            name='display_name',
            field=models.CharField(default='', max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
