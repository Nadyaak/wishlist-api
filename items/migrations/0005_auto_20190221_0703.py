# Generated by Django 2.1.5 on 2019-02-21 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_item_add_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='add_by',
            new_name='added_by',
        ),
        migrations.AlterField(
            model_name='favoriteitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Item'),
        ),
    ]