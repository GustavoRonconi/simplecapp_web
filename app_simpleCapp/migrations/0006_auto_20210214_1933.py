# Generated by Django 3.1.5 on 2021-02-14 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_simpleCapp', '0005_auto_20210214_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brokeragefeesmodel',
            name='end_date',
            field=models.DateField(null=True),
        ),
    ]
