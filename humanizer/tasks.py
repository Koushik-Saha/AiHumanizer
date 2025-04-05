# humanizer/tasks.py

from celery import shared_task

@shared_task
def humanize_text_task(content):
    # Dummy humanization logic; replace with real NLP processing later.
    return f"Humanized asynchronously: {content}"