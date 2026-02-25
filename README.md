# Marketing Campaigns Module

Plan, execute and track marketing campaigns.

## Features

- Create and manage marketing campaigns with multiple types (email, social, etc.)
- Track campaign lifecycle through statuses: Draft, Scheduled, Active, Paused, Completed
- Define campaign periods with start and end dates
- Set and monitor campaign budgets
- Dashboard overview of campaign performance
- Activate or deactivate campaigns

## Installation

This module is installed automatically via the ERPlora Marketplace.

## Configuration

Access settings via: **Menu > Marketing Campaigns > Settings**

## Usage

Access via: **Menu > Marketing Campaigns**

### Views

| View | URL | Description |
|------|-----|-------------|
| Dashboard | `/m/campaigns/dashboard/` | Overview of campaign metrics and status |
| Campaigns | `/m/campaigns/campaigns/` | List, create and manage campaigns |
| Settings | `/m/campaigns/settings/` | Module configuration |

## Models

| Model | Description |
|-------|-------------|
| `Campaign` | A marketing campaign with name, type, status, date range, budget, description, and active flag |

## Permissions

| Permission | Description |
|------------|-------------|
| `campaigns.view_campaign` | View campaigns |
| `campaigns.add_campaign` | Create new campaigns |
| `campaigns.change_campaign` | Edit existing campaigns |
| `campaigns.delete_campaign` | Delete campaigns |
| `campaigns.manage_settings` | Manage module settings |

## License

MIT

## Author

ERPlora Team - support@erplora.com
