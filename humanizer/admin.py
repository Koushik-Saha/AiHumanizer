from django.contrib import admin
from .models import Submission, APIKey, BannedPhrase

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_original', 'short_humanized', 'detection_evasion',
                    'plagiarism_score', 'flagged', 'created_at')
    list_filter = ('detection_evasion', 'plagiarism_check', 'flagged', 'created_at')
    search_fields = ('original_content', 'humanized_content')
    actions = ['mark_flagged', 'unmark_flagged']

    def short_original(self, obj):
        return obj.original_content[:50] + '...' if len(obj.original_content) > 50 else obj.original_content
    short_original.short_description = 'Original'

    def short_humanized(self, obj):
        return obj.humanized_content[:50] + '...' if len(obj.humanized_content) > 50 else obj.humanized_content
    short_humanized.short_description = 'Humanized'

    def mark_flagged(self, request, queryset):
        queryset.update(flagged=True)
    mark_flagged.short_description = "Mark selected submissions as flagged"

    def unmark_flagged(self, request, queryset):
        queryset.update(flagged=False)
    unmark_flagged.short_description = "Unmark selected submissions as flagged"

@admin.register(APIKey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = ('name', 'key', 'is_active', 'daily_count', 'daily_limit',
                    'monthly_count', 'monthly_limit', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'key')

@admin.register(BannedPhrase)
class BannedPhraseAdmin(admin.ModelAdmin):
    list_display = ('phrase', 'created_at')
    search_fields = ('phrase',)