# Generated by Django 3.2.3 on 2021-05-28 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20210526_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='showinSlideShow',
            field=models.BooleanField(default=False, verbose_name='يظهر في السلايد'),
        ),
    ]
