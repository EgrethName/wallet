# Generated by Django 3.2 on 2021-04-14 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_app', '0002_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='sum',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]
