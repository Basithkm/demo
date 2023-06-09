# Generated by Django 4.2.1 on 2023-05-15 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pro_rent', '0010_basedsize_rentproperty_per_size'),
        ('pro_sale', '0014_basedsize_sellproperty_per_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellproperty',
            name='per_size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pro_rent.basedsize'),
        ),
        migrations.DeleteModel(
            name='BasedSize',
        ),
    ]
