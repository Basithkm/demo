# Generated by Django 4.2.1 on 2023-05-15 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pro_rent', '0009_alter_rentproperty_rent_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasedSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('per_size', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='rentproperty',
            name='per_size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pro_rent.basedsize'),
        ),
    ]
