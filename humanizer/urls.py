from django.urls import path
from .views import HumanizeTextView, TaskStatusView

urlpatterns = [
    path('humanize-text/', HumanizeTextView.as_view(), name='humanize-text'),
    path('task-status/<str:task_id>/', TaskStatusView.as_view(), name='task-status'),
]