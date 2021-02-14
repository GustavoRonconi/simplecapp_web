from django.db import models


class BrokerModel(models.Model):
    class Meta:
        db_table = "broker"

    broker_name = models.CharField(max_length=50)
    
