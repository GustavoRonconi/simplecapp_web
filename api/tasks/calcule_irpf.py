from celery import shared_task
from api.models.financial_operations_model import FinancialOperationModel
from calcula 


@shared_task(bind=True)
def calcule_irpf(self, reference_year, profile_id, processed_irpf_id):
    financial_operations = FinancialOperationModel.objects.filter(
        profile_id=profile_id, date__year=reference_year
    )
    message_to_engine = {
        "profile_id": profile_id,
        "reference_year": reference_year,
        "financial_operations": [
            {
                "date": op.date,
                "operation_type": op.operation_type,
                "ticker": op.ticker,
                "ticker_type": op.ticker_type,
                "units": op.units,
                "unitary_value": op.unitary_value,
                "amount": op.amount,
                "broker": op.broker_id,
                "operation_class": op.operation_class,
                "currency_code": op.currency_code,
            }
            for op in financial_operations
        ],
    }
    print(1)
