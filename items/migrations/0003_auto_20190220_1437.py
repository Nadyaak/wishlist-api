# Generated by Django 2.1.5 on 2019-02-20 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_favoriteitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoriteitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to='items.Item'),
        ),
    ]
