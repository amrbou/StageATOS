# Generated by Django 5.0.7 on 2024-07-11 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='', max_length=255),
        ),
    ]
