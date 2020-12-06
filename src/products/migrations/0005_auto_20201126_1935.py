# Generated by Django 3.1.3 on 2020-11-26 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0004_auto_20201124_1544"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_price",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                max_digits=5,
                verbose_name="price of product",
            ),
        ),
    ]
