# Generated by Django 3.2.9 on 2021-11-16 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_producto_price'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Producto',
            new_name='Productos',
        ),
    ]
