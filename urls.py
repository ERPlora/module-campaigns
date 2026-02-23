from django.urls import path
from . import views

app_name = 'campaigns'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('campaigns/', views.campaigns, name='campaigns'),
    path('settings/', views.settings, name='settings'),
]
