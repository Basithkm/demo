# Generated by Django 4.2.1 on 2023-05-13 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro_rent', '0007_alter_rentproperty_rent_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentmessages',
            name='message',
        ),
        migrations.AddField(
            model_name='rentmessages',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='rentmessages',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='rentmessages',
            name='intrest',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='rentmessages',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]