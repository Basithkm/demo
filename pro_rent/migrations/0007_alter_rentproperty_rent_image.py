# Generated by Django 4.2 on 2023-05-08 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro_rent', '0006_alter_rentproperty_rent_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentproperty',
            name='rent_image',
            field=models.ImageField(blank=True, null=True, upload_to='rent_images'),
        ),
    ]
