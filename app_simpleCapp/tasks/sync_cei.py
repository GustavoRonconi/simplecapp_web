from celery import shared_task
from time import sleep
from celery_progress.backend import ProgressRecorder


@shared_task(bind=True)
def sync_cei(self, duration):
    progress_recorder = ProgressRecorder(self)
    for i in range(5):
        sleep(duration)
        progress_recorder.set_progress(i + 1, 5)
    return "Done"

