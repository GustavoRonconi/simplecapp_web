# Generated by Django 3.0.5 on 2020-04-17 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guiareceita', '0002_auto_20200417_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viagem',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
