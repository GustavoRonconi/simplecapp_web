from django.db import models


class BrokerageFeesModel(models.Model):
    class Meta:
        db_table = "brokerage_fees"

    begin_date = models.DateField(null=False)
    end_date = models.DateField(null=True)
    brokerage_fee_value = models.DecimalField(max_digits=10, decimal_places=5, null=False)
    broker = models.ForeignKey("BrokerModel", null=False, on_delete=models.CASCADE)
    profile = models.ForeignKey("ProfileModel", null=False, on_delete=models.CASCADE)
