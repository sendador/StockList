# Generated by Django 3.0.2 on 2020-01-29 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20200129_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocklist',
            name='stock_price',
            field=models.DecimalField(decimal_places=4, max_digits=20),
        ),
    ]
