# Generated by Django 3.1.5 on 2021-06-29 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210329_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='occupation',
            field=models.CharField(max_length=50, null=True),
        ),
    ]