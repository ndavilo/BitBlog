# Generated by Django 4.0 on 2022-02-08 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0002_cryptocoin_delete_binance_delete_bitcoin_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cryptocoin',
            old_name='Binance_value',
            new_name='binance_value',
        ),
        migrations.RenameField(
            model_name='cryptocoin',
            old_name='Bitcoin_value',
            new_name='bitcoin_value',
        ),
        migrations.RenameField(
            model_name='cryptocoin',
            old_name='Etherem_value',
            new_name='etherem_value',
        ),
        migrations.RenameField(
            model_name='cryptocoin',
            old_name='Tether_value',
            new_name='tether_value',
        ),
    ]
