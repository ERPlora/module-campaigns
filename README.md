# Marketing Campaigns

## Overview

| Property | Value |
|----------|-------|
| **Module ID** | `campaigns` |
| **Version** | `1.0.0` |
| **Icon** | `megaphone-outline` |
| **Dependencies** | None |

## Models

### `Campaign`

Campaign(id, hub_id, created_at, updated_at, created_by, updated_by, is_deleted, deleted_at, name, campaign_type, status, start_date, end_date, budget, description, is_active)

| Field | Type | Details |
|-------|------|---------|
| `name` | CharField | max_length=255 |
| `campaign_type` | CharField | max_length=30 |
| `status` | CharField | max_length=20, choices: draft, scheduled, active, paused, completed |
| `start_date` | DateField | optional |
| `end_date` | DateField | optional |
| `budget` | DecimalField |  |
| `description` | TextField | optional |
| `is_active` | BooleanField |  |

## URL Endpoints

Base path: `/m/campaigns/`

| Path | Name | Method |
|------|------|--------|
| `(root)` | `dashboard` | GET |
| `campaigns/` | `campaigns_list` | GET |
| `campaigns/add/` | `campaign_add` | GET/POST |
| `campaigns/<uuid:pk>/edit/` | `campaign_edit` | GET |
| `campaigns/<uuid:pk>/delete/` | `campaign_delete` | GET/POST |
| `campaigns/<uuid:pk>/toggle/` | `campaign_toggle_status` | GET |
| `campaigns/bulk/` | `campaigns_bulk_action` | GET/POST |
| `settings/` | `settings` | GET |

## Permissions

| Permission | Description |
|------------|-------------|
| `campaigns.view_campaign` | View Campaign |
| `campaigns.add_campaign` | Add Campaign |
| `campaigns.change_campaign` | Change Campaign |
| `campaigns.delete_campaign` | Delete Campaign |
| `campaigns.manage_settings` | Manage Settings |

**Role assignments:**

- **admin**: All permissions
- **manager**: `add_campaign`, `change_campaign`, `view_campaign`
- **employee**: `add_campaign`, `view_campaign`

## Navigation

| View | Icon | ID | Fullpage |
|------|------|----|----------|
| Dashboard | `speedometer-outline` | `dashboard` | No |
| Campaigns | `megaphone-outline` | `campaigns` | No |
| Settings | `settings-outline` | `settings` | No |

## AI Tools

Tools available for the AI assistant:

### `list_marketing_campaigns`

List marketing campaigns.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `status` | string | No | draft, scheduled, active, paused, completed |
| `campaign_type` | string | No |  |

### `create_marketing_campaign`

Create a marketing campaign.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes |  |
| `campaign_type` | string | No |  |
| `description` | string | No |  |
| `start_date` | string | No |  |
| `end_date` | string | No |  |
| `budget` | string | No |  |

## File Structure

```
README.md
__init__.py
admin.py
ai_tools.py
apps.py
forms.py
locale/
  en/
    LC_MESSAGES/
      django.po
  es/
    LC_MESSAGES/
      django.po
migrations/
  0001_initial.py
  __init__.py
models.py
module.py
static/
  campaigns/
    css/
    js/
  icons/
    icon.svg
templates/
  campaigns/
    pages/
      campaign_add.html
      campaign_edit.html
      campaigns.html
      dashboard.html
      index.html
      settings.html
    partials/
      campaign_add_content.html
      campaign_edit_content.html
      campaigns_content.html
      campaigns_list.html
      dashboard_content.html
      panel_campaign_add.html
      panel_campaign_edit.html
      settings_content.html
tests/
  __init__.py
  conftest.py
  test_models.py
  test_views.py
urls.py
views.py
```
