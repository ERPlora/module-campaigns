"""Tests for campaigns models."""
import pytest
from django.utils import timezone

from campaigns.models import Campaign


@pytest.mark.django_db
class TestCampaign:
    """Campaign model tests."""

    def test_create(self, campaign):
        """Test Campaign creation."""
        assert campaign.pk is not None
        assert campaign.is_deleted is False

    def test_str(self, campaign):
        """Test string representation."""
        assert str(campaign) is not None
        assert len(str(campaign)) > 0

    def test_soft_delete(self, campaign):
        """Test soft delete."""
        pk = campaign.pk
        campaign.is_deleted = True
        campaign.deleted_at = timezone.now()
        campaign.save()
        assert not Campaign.objects.filter(pk=pk).exists()
        assert Campaign.all_objects.filter(pk=pk).exists()

    def test_queryset_excludes_deleted(self, hub_id, campaign):
        """Test default queryset excludes deleted."""
        campaign.is_deleted = True
        campaign.deleted_at = timezone.now()
        campaign.save()
        assert Campaign.objects.filter(hub_id=hub_id).count() == 0

    def test_toggle_active(self, campaign):
        """Test toggling is_active."""
        original = campaign.is_active
        campaign.is_active = not original
        campaign.save()
        campaign.refresh_from_db()
        assert campaign.is_active != original


