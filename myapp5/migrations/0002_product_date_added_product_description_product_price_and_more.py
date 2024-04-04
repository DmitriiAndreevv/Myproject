# Generated by Django 5.0.3 on 2024-03-30 19:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp5', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=999999.99, max_digits=8),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=5.0, max_digits=3),
        ),
    ]
