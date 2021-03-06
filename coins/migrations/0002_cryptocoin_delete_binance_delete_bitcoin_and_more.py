# Generated by Django 4.0 on 2022-02-08 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cryptocoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bitcoin_value', models.FloatField()),
                ('Tether_value', models.FloatField()),
                ('Etherem_value', models.FloatField()),
                ('Binance_value', models.FloatField()),
                ('date_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Binance',
        ),
        migrations.DeleteModel(
            name='Bitcoin',
        ),
        migrations.DeleteModel(
            name='Ethereum',
        ),
        migrations.DeleteModel(
            name='Tether',
        ),
    ]
