# Generated by Django 3.1.5 on 2021-06-30 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_financialoperation"),
    ]

    operations = [
        migrations.AddField(
            model_name="financialoperation",
            name="profile",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="api.profilemodel"
            ),
            preserve_default=False,
        ),
    ]
