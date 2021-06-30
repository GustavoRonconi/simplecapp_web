from django.db.models.signals import post_save
from django.dispatch import receiver
from api.models.processed_irpf_model import ProcessedIRPFModel
from api.tasks.calcule_irpf import calcule_irpf


@receiver(post_save, sender=ProcessedIRPFModel)
def send_to_calcule_irpf(sender, instance, **kwargs):
    calcule_irpf.delay(instance.reference_year, instance.profile.id, instance.id)
