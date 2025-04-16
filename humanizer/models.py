from django.db import models

class Submission(models.Model):
    original_content = models.TextField()
    humanized_content = models.TextField()
    detection_evasion = models.BooleanField(default=False)
    plagiarism_check = models.BooleanField(default=False)
    plagiarism_score = models.IntegerField(null=True, blank=True)
    plagiarism_report_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission {self.id}"