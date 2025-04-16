from django.urls import path
from .views import HumanizeTextView, TaskStatusView

urlpatterns = [
    # Submit text for humanization (returns task_id)
    path('humanize-text/', HumanizeTextView.as_view(), name='humanize-text'),

    # Check task status / retrieve results
    path('task-status/<str:task_id>/', TaskStatusView.as_view(), name='task-status'),
]