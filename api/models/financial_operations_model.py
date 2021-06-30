from django.utils.translation import ugettext_lazy as _
from django.db import models


class FinancialOperationModel(models.Model):
    class OperationTypes(models.TextChoices):
        purchase = ("purchase", _("Compra"))
        sale = ("sale", _("Venda"))

    class OperationClasses(models.TextChoices):
        day_trade = ("day_trade", _("DayTrade"))
        normal = ("normal", _("Normal"))

    class TickerTypes(models.TextChoices):
        stock = ("stock", _("Ações"))
        fiis = ("fiis", _("Fundos Imobiliários"))
        bdr = ("bdr", _("BDR"))

    class Meta:
        db_table = "financial_operation"

    date = models.DateField()
    operation_type = models.CharField(
        choices=OperationTypes.choices, max_length=8)
    operation_class = models.CharField(
        choices=OperationClasses.choices, max_length=9)
    ticker = models.CharField(max_length=50)
    ticker_type = models.CharField(choices=TickerTypes.choices, max_length=5)
    units = models.DecimalField(max_digits=10, decimal_places=5)
    unitary_value = models.DecimalField(max_digits=10, decimal_places=5)
    amount = models.DecimalField(max_digits=10, decimal_places=5)
    broker = models.ForeignKey(
        "BrokerModel", on_delete=models.PROTECT)
    profile = models.ForeignKey("ProfileModel", on_delete=models.CASCADE)
    currency_code = models.CharField(max_length=50)
