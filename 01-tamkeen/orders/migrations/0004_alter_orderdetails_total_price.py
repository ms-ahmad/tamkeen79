# Generated by Django 3.2.3 on 2021-06-09 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_orderdetails_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='total_price',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='مجموع السعر'),
        ),
    ]