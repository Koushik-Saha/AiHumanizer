# humanizer/tasks.py

from celery import shared_task

from humanizer.humanizer_engine import humanize_text


@shared_task
def humanize_text_task(content):
    # Use the humanization engine to transform the text
    result = humanize_text(content)
    return result