# Generated by Django 3.1.5 on 2021-02-08 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_simpleCapp', '0002_auto_20210129_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='cpf',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
