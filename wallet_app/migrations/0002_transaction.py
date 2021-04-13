# Generated by Django 3.2 on 2021-04-12 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('sum', models.IntegerField(default=0)),
                ('comment', models.CharField(max_length=255)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet_app.wallet')),
            ],
        ),
    ]
