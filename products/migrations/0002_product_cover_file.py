# Generated by Django 4.0.2 on 2024-07-05 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cover_file',
            field=models.ImageField(default='abc.jpg', upload_to=''),
            preserve_default=False,
        ),
    ]
