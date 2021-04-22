# Generated by Django 3.1.5 on 2021-04-18 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creditor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('transactionCtr', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.IntegerField(default=0)),
                ('account', models.CharField(max_length=24)),
                ('direction', models.BooleanField()),
                ('date', models.DateTimeField(verbose_name='date transacted')),
                ('value', models.CharField(max_length=10)),
                ('verwendungszweck', models.CharField(max_length=300)),
                ('textBooking', models.CharField(max_length=300)),
                ('customer', models.CharField(max_length=300)),
                ('BLZ', models.CharField(max_length=14)),
                ('creditorId', models.CharField(max_length=40)),
                ('mandat', models.CharField(max_length=40)),
                ('customerReference', models.CharField(max_length=40)),
                ('category', models.CharField(max_length=40)),
                ('types', models.CharField(max_length=40)),
                ('tags', models.CharField(max_length=40)),
                ('creditor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loader.creditor')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('nrTransactions', models.IntegerField(default=0)),
                ('firstTransact', models.DateTimeField(verbose_name='pub_date')),
                ('lastTransact', models.DateTimeField(verbose_name='pub_date')),
                ('dateCreated', models.DateTimeField(verbose_name='pub_date')),
                ('dateUpdated', models.DateTimeField(verbose_name='pub_date')),
                ('transactions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loader.transaction')),
            ],
        ),
    ]
