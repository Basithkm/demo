# Generated by Django 4.2.1 on 2023-05-15 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro_sale', '0009_sellproperty_image_height_sellproperty_image_width_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellproperty',
            name='image_height',
        ),
        migrations.RemoveField(
            model_name='sellproperty',
            name='image_width',
        ),
        migrations.AlterField(
            model_name='sellproperty',
            name='rent_image',
            field=models.ImageField(blank=True, null=True, upload_to='rent_images/'),
        ),
    ]
