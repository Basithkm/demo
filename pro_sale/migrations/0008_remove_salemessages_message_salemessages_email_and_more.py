# Generated by Django 4.2.1 on 2023-05-13 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro_sale', '0007_delete_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salemessages',
            name='message',
        ),
        migrations.AddField(
            model_name='salemessages',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='salemessages',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='salemessages',
            name='intrest',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='salemessages',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
