from celery import shared_task
from time import sleep
from celery_progress.backend import ProgressRecorder
from ..utils import send_notifications


@shared_task(bind=True)
def generate_report(self, duration):
    progress_recorder = ProgressRecorder(self)
    for i in range(5):
        sleep(duration)
        progress_recorder.set_progress(i + 1, 5)

    send_notifications("Não é que esse negócio funciona?", all_user=True)

    return "Done"
