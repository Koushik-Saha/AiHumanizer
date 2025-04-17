from django.urls import path
from .views import HumanizeTextView, TaskStatusView, ExportSubmissionView, SentenceEditorView, RegisterView, LoginView

urlpatterns = [
    # Submit text for humanization (returns task_id)
    path('humanize-text/', HumanizeTextView.as_view(), name='humanize-text'),

    # Check task status / retrieve results
    path('task-status/<str:task_id>/', TaskStatusView.as_view(), name='task-status'),

    path('export/<int:submission_id>/', ExportSubmissionView.as_view(), name='export-submission'),

    path('sentence-editor/', SentenceEditorView.as_view(), name='sentence-editor'),

    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),

]