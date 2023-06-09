# Generated by Django 4.2.1 on 2023-06-01 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('unit_cost', models.DecimalField(decimal_places=2, max_digits=40)),
                ('sales_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('qty_on_hand', models.IntegerField()),
                ('qty_reserved', models.IntegerField(default=0)),
            ],
        ),
    ]
