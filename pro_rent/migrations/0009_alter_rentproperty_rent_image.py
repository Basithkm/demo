# Generated by Django 4.2.1 on 2023-05-15 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro_rent', '0008_remove_rentmessages_message_rentmessages_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentproperty',
            name='rent_image',
            field=models.ImageField(blank=True, help_text='sale images', null=True, upload_to='sale_images/', verbose_name='sale images'),
        ),
    ]
