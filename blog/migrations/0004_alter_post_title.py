# Generated by Django 4.0.1 on 2022-01-20 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default=' SELL OR BUY COIN', max_length=50),
        ),
    ]
