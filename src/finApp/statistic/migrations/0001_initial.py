# Generated by Django 3.1.5 on 2021-08-12 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('klasse', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(default='', max_length=24)),
                ('value', models.CharField(default='', max_length=10)),
                ('aim', models.CharField(default='', max_length=300)),
                ('textBooking', models.CharField(default='', max_length=300)),
                ('customer', models.CharField(default='', max_length=300)),
                ('blz', models.CharField(max_length=14)),
                ('creditorId', models.CharField(default='', max_length=40)),
                ('mandat', models.CharField(default='', max_length=40)),
                ('customerReference', models.CharField(default='', max_length=40)),
                ('date', models.DateTimeField()),
                ('cathegory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='statistic.category')),
                ('classification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='statistic.classification')),
                ('tags', models.ManyToManyField(blank=True, null=True, to='statistic.Tags')),
            ],
        ),
    ]
