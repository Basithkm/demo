# Generated by Django 4.2.1 on 2023-05-16 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro_rent', '0011_alter_rentproperty_daily_rent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentproperty',
            name='upload_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
