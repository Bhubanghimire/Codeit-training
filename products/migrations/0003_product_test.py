# Generated by Django 4.0.2 on 2024-07-05 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_cover_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='test',
            field=models.TextField(blank=True, null=True),
        ),
    ]
