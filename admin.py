from django.contrib import admin

from .models import Campaign

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ['name', 'campaign_type', 'status', 'start_date', 'end_date', 'created_at']
    search_fields = ['name', 'campaign_type', 'status', 'description']
    readonly_fields = ['created_at', 'updated_at']

