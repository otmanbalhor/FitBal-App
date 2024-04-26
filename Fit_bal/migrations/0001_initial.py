# Generated by Django 5.0.4 on 2024-04-26 08:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=128)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('P', 'Other')], max_length=1)),
                ('age', models.CharField(max_length=12)),
                ('price', models.FloatField()),
                ('city', models.CharField(max_length=32)),
                ('zip_code', models.CharField(max_length=16)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('save_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Coach',
                'verbose_name_plural': 'Coachs',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=128)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('P', 'Other')], max_length=1)),
                ('age', models.CharField(max_length=12)),
                ('city', models.CharField(max_length=32)),
                ('zip_code', models.CharField(max_length=16)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('save_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_datetime', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=100000)),
                ('last_updated_date', models.DateTimeField(blank=True, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('comment', models.TextField(blank=True, max_length=1000, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Fit_bal.customer')),
                ('save_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Invoice',
                'verbose_name_plural': 'Invoices',
            },
        ),
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('P', 'Premium'), ('S', 'Standard')], max_length=1)),
                ('quantity', models.IntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('total', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fit_bal.invoice')),
            ],
            options={
                'verbose_name': 'Subscription',
                'verbose_name_plural': 'Subscriptions',
            },
        ),
    ]
