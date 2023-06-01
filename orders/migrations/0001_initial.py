# Generated by Django 4.2.1 on 2023-06-01 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('status', models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('I', 'Issued'), ('C', 'Cancelled')], default='I', max_length=3)),
                ('cart', models.ManyToManyField(related_name='orders', to='inventory.product')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='accounts.customer')),
            ],
        ),
    ]
