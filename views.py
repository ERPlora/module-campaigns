"""
Marketing Campaigns Module Views
"""
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from apps.accounts.decorators import login_required
from apps.core.htmx import htmx_view
from apps.modules_runtime.navigation import with_module_nav


@login_required
@with_module_nav('campaigns', 'dashboard')
@htmx_view('campaigns/pages/dashboard.html', 'campaigns/partials/dashboard_content.html')
def dashboard(request):
    """Dashboard view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('campaigns', 'campaigns')
@htmx_view('campaigns/pages/campaigns.html', 'campaigns/partials/campaigns_content.html')
def campaigns(request):
    """Campaigns view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('campaigns', 'settings')
@htmx_view('campaigns/pages/settings.html', 'campaigns/partials/settings_content.html')
def settings(request):
    """Settings view."""
    hub_id = request.session.get('hub_id')
    return {}

