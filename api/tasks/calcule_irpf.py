from celery import shared_task
from time import sleep


@shared_task(bind=True)
def calcule_irpf(self, reference_year, profile, processed_irpf_id):
    for i in range(5):
        sleep(2)
    print(reference_year, profile, processed_irpf_id)
    return
