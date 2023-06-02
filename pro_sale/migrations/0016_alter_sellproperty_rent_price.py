# Generated by Django 4.2.1 on 2023-05-15 12:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro_sale', '0015_alter_sellproperty_per_size_delete_basedsize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellproperty',
            name='rent_price',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]