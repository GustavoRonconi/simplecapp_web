from django.db import models


class States(models.Model):
    name = models.CharField(max_length=96)
    state_abbr = models.CharField(max_length=24, blank=True)
