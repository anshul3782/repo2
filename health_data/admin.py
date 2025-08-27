from django.contrib import admin
from .models import HealthData

@admin.register(HealthData)
class HealthDataAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'username', 'steps', 'avg_heart_rate', 'resting_calories', 'sleep_hours', 'updated_at']
    list_filter = ['updated_at', 'created_at']
    search_fields = ['phone_number']
    readonly_fields = ['created_at', 'updated_at', 'username']
    
    fieldsets = (
        ('User Information', {
            'fields': ('phone_number', 'username')
        }),
        ('Health Metrics', {
            'fields': ('steps', 'avg_heart_rate', 'resting_calories', 'sleep_hours')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
