from django.db import models
from django.utils.timezone import now


class ProcessedIRPFModel(models.Model):
    class Meta:
        db_table = "processed_irpf"

    reference_year = models.IntegerField()
    profile = models.ForeignKey("ProfileModel", on_delete=models.CASCADE)
    processing_datetime = models.DateTimeField(default=now, editable=False)
