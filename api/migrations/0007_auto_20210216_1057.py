# Generated by Django 3.1.5 on 2021-02-16 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210214_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brokeragefeesmodel',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.profilemodel'),
        ),
    ]