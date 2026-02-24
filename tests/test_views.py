"""Tests for campaigns views."""
import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestDashboard:
    """Dashboard view tests."""

    def test_dashboard_loads(self, auth_client):
        """Test dashboard page loads."""
        url = reverse('campaigns:dashboard')
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_dashboard_htmx(self, auth_client):
        """Test dashboard HTMX partial."""
        url = reverse('campaigns:dashboard')
        response = auth_client.get(url, HTTP_HX_REQUEST='true')
        assert response.status_code == 200

    def test_dashboard_requires_auth(self, client):
        """Test dashboard requires authentication."""
        url = reverse('campaigns:dashboard')
        response = client.get(url)
        assert response.status_code == 302


@pytest.mark.django_db
class TestCampaignViews:
    """Campaign view tests."""

    def test_list_loads(self, auth_client):
        """Test list view loads."""
        url = reverse('campaigns:campaigns_list')
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_list_htmx(self, auth_client):
        """Test list HTMX partial."""
        url = reverse('campaigns:campaigns_list')
        response = auth_client.get(url, HTTP_HX_REQUEST='true')
        assert response.status_code == 200

    def test_list_search(self, auth_client):
        """Test list search."""
        url = reverse('campaigns:campaigns_list')
        response = auth_client.get(url, {'q': 'test'})
        assert response.status_code == 200

    def test_list_sort(self, auth_client):
        """Test list sorting."""
        url = reverse('campaigns:campaigns_list')
        response = auth_client.get(url, {'sort': 'created_at', 'dir': 'desc'})
        assert response.status_code == 200

    def test_export_csv(self, auth_client):
        """Test CSV export."""
        url = reverse('campaigns:campaigns_list')
        response = auth_client.get(url, {'export': 'csv'})
        assert response.status_code == 200
        assert 'text/csv' in response['Content-Type']

    def test_export_excel(self, auth_client):
        """Test Excel export."""
        url = reverse('campaigns:campaigns_list')
        response = auth_client.get(url, {'export': 'excel'})
        assert response.status_code == 200

    def test_add_form_loads(self, auth_client):
        """Test add form loads."""
        url = reverse('campaigns:campaign_add')
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_add_post(self, auth_client):
        """Test creating via POST."""
        url = reverse('campaigns:campaign_add')
        data = {
            'name': 'New Name',
            'campaign_type': 'New Campaign Type',
            'status': 'New Status',
            'start_date': '2025-01-15',
            'end_date': '2025-01-15',
        }
        response = auth_client.post(url, data)
        assert response.status_code == 200

    def test_edit_form_loads(self, auth_client, campaign):
        """Test edit form loads."""
        url = reverse('campaigns:campaign_edit', args=[campaign.pk])
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_edit_post(self, auth_client, campaign):
        """Test editing via POST."""
        url = reverse('campaigns:campaign_edit', args=[campaign.pk])
        data = {
            'name': 'Updated Name',
            'campaign_type': 'Updated Campaign Type',
            'status': 'Updated Status',
            'start_date': '2025-01-15',
            'end_date': '2025-01-15',
        }
        response = auth_client.post(url, data)
        assert response.status_code == 200

    def test_delete(self, auth_client, campaign):
        """Test soft delete via POST."""
        url = reverse('campaigns:campaign_delete', args=[campaign.pk])
        response = auth_client.post(url)
        assert response.status_code == 200
        campaign.refresh_from_db()
        assert campaign.is_deleted is True

    def test_toggle_status(self, auth_client, campaign):
        """Test toggle active status."""
        url = reverse('campaigns:campaign_toggle_status', args=[campaign.pk])
        original = campaign.is_active
        response = auth_client.post(url)
        assert response.status_code == 200
        campaign.refresh_from_db()
        assert campaign.is_active != original

    def test_bulk_delete(self, auth_client, campaign):
        """Test bulk delete."""
        url = reverse('campaigns:campaigns_bulk_action')
        response = auth_client.post(url, {'ids': str(campaign.pk), 'action': 'delete'})
        assert response.status_code == 200
        campaign.refresh_from_db()
        assert campaign.is_deleted is True

    def test_list_requires_auth(self, client):
        """Test list requires authentication."""
        url = reverse('campaigns:campaigns_list')
        response = client.get(url)
        assert response.status_code == 302


@pytest.mark.django_db
class TestSettings:
    """Settings view tests."""

    def test_settings_loads(self, auth_client):
        """Test settings page loads."""
        url = reverse('campaigns:settings')
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_settings_requires_auth(self, client):
        """Test settings requires authentication."""
        url = reverse('campaigns:settings')
        response = client.get(url)
        assert response.status_code == 302

