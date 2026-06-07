from django.contrib import admin

from .models import Word


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ("word", "meaning_preview", "created_at")
    search_fields = ("word", "meaning")
    ordering = ("-created_at",)

    def meaning_preview(self, obj):
        return obj.meaning[:40]

    meaning_preview.short_description = "意味"
