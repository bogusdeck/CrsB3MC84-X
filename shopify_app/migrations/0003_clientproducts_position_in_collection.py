# Generated by Django 5.1.1 on 2024-10-05 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopify_app', '0002_clientcollections_collection_total_revenue_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientproducts',
            name='position_in_collection',
            field=models.IntegerField(default=0),
        ),
    ]
