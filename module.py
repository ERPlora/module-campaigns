    from django.utils.translation import gettext_lazy as _

    MODULE_ID = 'campaigns'
    MODULE_NAME = _('Marketing Campaigns')
    MODULE_VERSION = '1.0.0'
    MODULE_ICON = 'megaphone-outline'
    MODULE_DESCRIPTION = _('Plan, execute and track marketing campaigns')
    MODULE_AUTHOR = 'ERPlora'
    MODULE_CATEGORY = 'marketing'

    MENU = {
        'label': _('Marketing Campaigns'),
        'icon': 'megaphone-outline',
        'order': 52,
    }

    NAVIGATION = [
        {'label': _('Dashboard'), 'icon': 'speedometer-outline', 'id': 'dashboard'},
{'label': _('Campaigns'), 'icon': 'megaphone-outline', 'id': 'campaigns'},
{'label': _('Settings'), 'icon': 'settings-outline', 'id': 'settings'},
    ]

    DEPENDENCIES = []

    PERMISSIONS = [
        'campaigns.view_campaign',
'campaigns.add_campaign',
'campaigns.change_campaign',
'campaigns.delete_campaign',
'campaigns.manage_settings',
    ]
