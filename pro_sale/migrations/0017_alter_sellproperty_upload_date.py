# Generated by Django 4.2.1 on 2023-05-16 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro_sale', '0016_alter_sellproperty_rent_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellproperty',
            name='upload_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
