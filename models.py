from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models.base import HubBaseModel

CAMPAIGN_STATUS = [
    ('draft', _('Draft')),
    ('scheduled', _('Scheduled')),
    ('active', _('Active')),
    ('paused', _('Paused')),
    ('completed', _('Completed')),
]

class Campaign(HubBaseModel):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    campaign_type = models.CharField(max_length=30, default='email', verbose_name=_('Campaign Type'))
    status = models.CharField(max_length=20, default='draft', choices=CAMPAIGN_STATUS, verbose_name=_('Status'))
    start_date = models.DateField(null=True, blank=True, verbose_name=_('Start Date'))
    end_date = models.DateField(null=True, blank=True, verbose_name=_('End Date'))
    budget = models.DecimalField(max_digits=12, decimal_places=2, default='0', verbose_name=_('Budget'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is Active'))

    class Meta(HubBaseModel.Meta):
        db_table = 'campaigns_campaign'

    def __str__(self):
        return self.name

