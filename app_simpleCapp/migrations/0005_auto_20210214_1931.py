# Generated by Django 3.1.5 on 2021-02-14 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_simpleCapp', '0004_brokeragefeesmodel_brokermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brokeragefeesmodel',
            name='brokerage_fee_value',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
    ]
