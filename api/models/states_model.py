from django.db import models


class StatesModel(models.Model):
    class Meta:
        db_table = "states"

    name = models.CharField(max_length=96, null=False)
    state_abbr = models.CharField(max_length=24, null=False)
    cod_uf = models.IntegerField(null=False)
