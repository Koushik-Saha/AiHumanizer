from celery import shared_task
from .humanizer_engine import humanize_text
from .plagiarism_checker import check_plagiarism
from .models import Submission

@shared_task
def humanize_text_task(content, detection_evasion=False, plagiarism_check=False):
    # Optional plagiarism check
    plagiarism_result = None
    if plagiarism_check:
        plagiarism_result = check_plagiarism(content)

    # Humanize the content
    humanized = humanize_text(content, detection_evasion)

    # Save submission
    submission = Submission.objects.create(
        original_content=content,
        humanized_content=humanized,
        detection_evasion=detection_evasion,
        plagiarism_check=plagiarism_check,
        plagiarism_score=(plagiarism_result.get("score") if plagiarism_result else None),
        plagiarism_report_url=(plagiarism_result.get("report_url") if plagiarism_result else None)
    )

    # Return submission ID alongside results
    return {
        "submission_id": submission.id,
        "humanized_content": humanized,
        "plagiarism": plagiarism_result
    }