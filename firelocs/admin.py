from django.contrib import admin

from firelocs.models import Incident


@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = (
        "location",
        "fire_type",
        "fire_status",
        "alert_level",
        "council_area",
    )
    list_filter = ("fire_status", "fire_type")
