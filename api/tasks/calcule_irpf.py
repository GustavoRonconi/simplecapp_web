from celery import shared_task
from api.models.financial_operations_model import FinancialOperationModel
from simplecapp_calculation_engine import CalculationEngine, calculation_engine


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
    calculation_engine_instance = CalculationEngine(message_to_engine)
    output_irpf = calculation_engine_instance.process()

    # TODO criar os modelos de saída p/ persistir no banco
