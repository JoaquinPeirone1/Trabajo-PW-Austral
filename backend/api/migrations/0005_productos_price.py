# Generated by Django 3.2.9 on 2021-11-16 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_producto_productos'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='price',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
