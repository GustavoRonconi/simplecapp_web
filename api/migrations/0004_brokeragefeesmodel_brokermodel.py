# Generated by Django 3.1.5 on 2021-02-14 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210208_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrokerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('broker_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'broker',
            },
        ),
        migrations.CreateModel(
            name='BrokerageFeesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin_date', models.DateField()),
                ('end_date', models.DateField()),
                ('brokerage_fee_value', models.DecimalField(decimal_places=5, max_digits=5)),
                ('broker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.brokermodel')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.statesmodel')),
            ],
            options={
                'db_table': 'brokerage_fees',
            },
        ),
    ]