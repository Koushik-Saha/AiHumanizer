from celery import shared_task
from .humanizer_engine import humanize_text
from .plagiarism_checker import check_plagiarism

@shared_task
def humanize_text_task(content, detection_evasion=False, plagiarism_check=False):
    # Optional plagiarism check
    plagiarism_result = None
    if plagiarism_check:
        plagiarism_result = check_plagiarism(content)

    # Humanize the content
    humanized = humanize_text(content, detection_evasion)

    # Build the result payload
    return {
        "humanized_content": humanized,
        "plagiarism": plagiarism_result
    }