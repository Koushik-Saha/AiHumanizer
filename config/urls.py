from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    # Humanizer API endpoints
    path('api/', include('humanizer.urls')),
]