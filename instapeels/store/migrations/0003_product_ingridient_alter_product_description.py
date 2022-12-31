# Generated by Django 4.0.3 on 2022-12-30 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ingridient',
            field=models.TextField(default=False, max_length=500, verbose_name='Ingridient'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=600, verbose_name='Description'),
        ),
    ]
