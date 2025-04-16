import uuid
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

class APIKey(models.Model):
    key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    daily_limit = models.IntegerField(default=1000)       # requests per day
    daily_count = models.IntegerField(default=0)          # counter for today
    monthly_limit = models.IntegerField(default=10000)    # total requests per month
    monthly_count = models.IntegerField(default=0)        # counter for month

    def __str__(self):
        return f"{self.name} ({self.key})"