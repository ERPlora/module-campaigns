"""
Marketing Campaigns Module Views
"""
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.shortcuts import get_object_or_404, render as django_render
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_POST

from apps.accounts.decorators import login_required, permission_required
from apps.core.htmx import htmx_view
from apps.core.services import export_to_csv, export_to_excel
from apps.modules_runtime.navigation import with_module_nav

from .models import Campaign

PER_PAGE_CHOICES = [10, 25, 50, 100]


# ======================================================================
# Dashboard
# ======================================================================

@login_required
@with_module_nav('campaigns', 'dashboard')
@htmx_view('campaigns/pages/index.html', 'campaigns/partials/dashboard_content.html')
def dashboard(request):
    hub_id = request.session.get('hub_id')
    return {
        'total_campaigns': Campaign.objects.filter(hub_id=hub_id, is_deleted=False).count(),
    }


# ======================================================================
# Campaign
# ======================================================================

CAMPAIGN_SORT_FIELDS = {
    'name': 'name',
    'status': 'status',
    'is_active': 'is_active',
    'budget': 'budget',
    'campaign_type': 'campaign_type',
    'start_date': 'start_date',
    'created_at': 'created_at',
}

def _build_campaigns_context(hub_id, per_page=10):
    qs = Campaign.objects.filter(hub_id=hub_id, is_deleted=False).order_by('name')
    paginator = Paginator(qs, per_page)
    page_obj = paginator.get_page(1)
    return {
        'campaigns': page_obj,
        'page_obj': page_obj,
        'search_query': '',
        'sort_field': 'name',
        'sort_dir': 'asc',
        'current_view': 'table',
        'per_page': per_page,
    }

def _render_campaigns_list(request, hub_id, per_page=10):
    ctx = _build_campaigns_context(hub_id, per_page)
    return django_render(request, 'campaigns/partials/campaigns_list.html', ctx)

@login_required
@with_module_nav('campaigns', 'campaigns')
@htmx_view('campaigns/pages/campaigns.html', 'campaigns/partials/campaigns_content.html')
def campaigns_list(request):
    hub_id = request.session.get('hub_id')
    search_query = request.GET.get('q', '').strip()
    sort_field = request.GET.get('sort', 'name')
    sort_dir = request.GET.get('dir', 'asc')
    page_number = request.GET.get('page', 1)
    current_view = request.GET.get('view', 'table')
    per_page = int(request.GET.get('per_page', 10))
    if per_page not in PER_PAGE_CHOICES:
        per_page = 10

    qs = Campaign.objects.filter(hub_id=hub_id, is_deleted=False)

    if search_query:
        qs = qs.filter(Q(name__icontains=search_query) | Q(campaign_type__icontains=search_query) | Q(status__icontains=search_query) | Q(description__icontains=search_query))

    order_by = CAMPAIGN_SORT_FIELDS.get(sort_field, 'name')
    if sort_dir == 'desc':
        order_by = f'-{order_by}'
    qs = qs.order_by(order_by)

    export_format = request.GET.get('export')
    if export_format in ('csv', 'excel'):
        fields = ['name', 'status', 'is_active', 'budget', 'campaign_type', 'start_date']
        headers = ['Name', 'Status', 'Is Active', 'Budget', 'Campaign Type', 'Start Date']
        if export_format == 'csv':
            return export_to_csv(qs, fields=fields, headers=headers, filename='campaigns.csv')
        return export_to_excel(qs, fields=fields, headers=headers, filename='campaigns.xlsx')

    paginator = Paginator(qs, per_page)
    page_obj = paginator.get_page(page_number)

    if request.htmx and request.htmx.target == 'datatable-body':
        return django_render(request, 'campaigns/partials/campaigns_list.html', {
            'campaigns': page_obj, 'page_obj': page_obj,
            'search_query': search_query, 'sort_field': sort_field,
            'sort_dir': sort_dir, 'current_view': current_view, 'per_page': per_page,
        })

    return {
        'campaigns': page_obj, 'page_obj': page_obj,
        'search_query': search_query, 'sort_field': sort_field,
        'sort_dir': sort_dir, 'current_view': current_view, 'per_page': per_page,
    }

@login_required
def campaign_add(request):
    hub_id = request.session.get('hub_id')
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        campaign_type = request.POST.get('campaign_type', '').strip()
        status = request.POST.get('status', '').strip()
        start_date = request.POST.get('start_date') or None
        end_date = request.POST.get('end_date') or None
        budget = request.POST.get('budget', '0') or '0'
        description = request.POST.get('description', '').strip()
        is_active = request.POST.get('is_active') == 'on'
        obj = Campaign(hub_id=hub_id)
        obj.name = name
        obj.campaign_type = campaign_type
        obj.status = status
        obj.start_date = start_date
        obj.end_date = end_date
        obj.budget = budget
        obj.description = description
        obj.is_active = is_active
        obj.save()
        return _render_campaigns_list(request, hub_id)
    return django_render(request, 'campaigns/partials/panel_campaign_add.html', {})

@login_required
def campaign_edit(request, pk):
    hub_id = request.session.get('hub_id')
    obj = get_object_or_404(Campaign, pk=pk, hub_id=hub_id, is_deleted=False)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '').strip()
        obj.campaign_type = request.POST.get('campaign_type', '').strip()
        obj.status = request.POST.get('status', '').strip()
        obj.start_date = request.POST.get('start_date') or None
        obj.end_date = request.POST.get('end_date') or None
        obj.budget = request.POST.get('budget', '0') or '0'
        obj.description = request.POST.get('description', '').strip()
        obj.is_active = request.POST.get('is_active') == 'on'
        obj.save()
        return _render_campaigns_list(request, hub_id)
    return django_render(request, 'campaigns/partials/panel_campaign_edit.html', {'obj': obj})

@login_required
@require_POST
def campaign_delete(request, pk):
    hub_id = request.session.get('hub_id')
    obj = get_object_or_404(Campaign, pk=pk, hub_id=hub_id, is_deleted=False)
    obj.is_deleted = True
    obj.deleted_at = timezone.now()
    obj.save(update_fields=['is_deleted', 'deleted_at', 'updated_at'])
    return _render_campaigns_list(request, hub_id)

@login_required
@require_POST
def campaign_toggle_status(request, pk):
    hub_id = request.session.get('hub_id')
    obj = get_object_or_404(Campaign, pk=pk, hub_id=hub_id, is_deleted=False)
    obj.is_active = not obj.is_active
    obj.save(update_fields=['is_active', 'updated_at'])
    return _render_campaigns_list(request, hub_id)

@login_required
@require_POST
def campaigns_bulk_action(request):
    hub_id = request.session.get('hub_id')
    ids = [i.strip() for i in request.POST.get('ids', '').split(',') if i.strip()]
    action = request.POST.get('action', '')
    qs = Campaign.objects.filter(hub_id=hub_id, is_deleted=False, id__in=ids)
    if action == 'activate':
        qs.update(is_active=True)
    elif action == 'deactivate':
        qs.update(is_active=False)
    elif action == 'delete':
        qs.update(is_deleted=True, deleted_at=timezone.now())
    return _render_campaigns_list(request, hub_id)


@login_required
@permission_required('campaigns.manage_settings')
@with_module_nav('campaigns', 'settings')
@htmx_view('campaigns/pages/settings.html', 'campaigns/partials/settings_content.html')
def settings_view(request):
    return {}

