"""
AI context for the Campaigns module.
Loaded into the assistant system prompt when this module's tools are active.
"""

CONTEXT = """
## Module Knowledge: Campaigns

### Models

**Campaign** — A marketing campaign (email, social, etc.).
- `name`
- `campaign_type` (CharField, default 'email'): Type of campaign (e.g., 'email', 'sms', 'social', 'event')
- `status`: 'draft' | 'scheduled' | 'active' | 'paused' | 'completed'
- `start_date`, `end_date` (DateField, optional)
- `budget` (Decimal, default 0)
- `description`
- `is_active` (bool)

### Key Flows

1. **Create campaign**: Create Campaign with name, type, dates, budget (status='draft')
2. **Schedule**: Set start_date and update status to 'scheduled'
3. **Activate**: On start_date, set status='active'; begin sending/running
4. **Pause**: Set status='paused' to temporarily stop the campaign
5. **Complete**: Set status='completed' when campaign ends or is manually closed

### Notes
- This is a lightweight campaign tracking model. It records campaigns and their metadata but does not include built-in audience/recipient management or email sending.
- For audience targeting, use the Segments module to identify customers.
- Budget tracking is manual — no automatic spend tracking.
"""
