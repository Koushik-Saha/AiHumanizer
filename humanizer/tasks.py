from celery import shared_task
from .humanizer_engine import humanize_text

@shared_task
def humanize_text_task(content, detection_evasion=False):
    # Use the humanization engine with the detection evasion flag
    result = humanize_text(content, detection_evasion)
    return result