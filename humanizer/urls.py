from django.urls import path
from .views import HumanizeTextView

urlpatterns = [
    path('humanize-text/', HumanizeTextView.as_view(), name='humanize-text'),
]