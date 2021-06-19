# Generated by Django 3.2.3 on 2021-06-08 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='adderess',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='العنوان'),
        ),
        migrations.AlterField(
            model_name='order',
            name='gover',
            field=models.CharField(blank=True, choices=[('b', 'بغداد'), ('m', 'محافظات')], max_length=1, null=True, verbose_name='المحافظة'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='الهاتف'),
        ),
    ]