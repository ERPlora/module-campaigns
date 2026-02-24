from django.urls import path
from . import views

app_name = 'campaigns'

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Campaign
    path('campaigns/', views.campaigns_list, name='campaigns_list'),
    path('campaigns/add/', views.campaign_add, name='campaign_add'),
    path('campaigns/<uuid:pk>/edit/', views.campaign_edit, name='campaign_edit'),
    path('campaigns/<uuid:pk>/delete/', views.campaign_delete, name='campaign_delete'),
    path('campaigns/<uuid:pk>/toggle/', views.campaign_toggle_status, name='campaign_toggle_status'),
    path('campaigns/bulk/', views.campaigns_bulk_action, name='campaigns_bulk_action'),

    # Settings
    path('settings/', views.settings_view, name='settings'),
]
