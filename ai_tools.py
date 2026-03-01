"""AI tools for the Campaigns module."""
from assistant.tools import AssistantTool, register_tool


@register_tool
class ListCampaigns(AssistantTool):
    name = "list_marketing_campaigns"
    description = "List marketing campaigns."
    module_id = "campaigns"
    required_permission = "campaigns.view_campaign"
    parameters = {
        "type": "object",
        "properties": {"status": {"type": "string", "description": "draft, scheduled, active, paused, completed"}, "campaign_type": {"type": "string"}},
        "required": [],
        "additionalProperties": False,
    }

    def execute(self, args, request):
        from campaigns.models import Campaign
        qs = Campaign.objects.all()
        if args.get('status'):
            qs = qs.filter(status=args['status'])
        if args.get('campaign_type'):
            qs = qs.filter(campaign_type=args['campaign_type'])
        return {"campaigns": [{"id": str(c.id), "name": c.name, "campaign_type": c.campaign_type, "status": c.status, "start_date": str(c.start_date) if c.start_date else None, "end_date": str(c.end_date) if c.end_date else None, "budget": str(c.budget) if c.budget else None} for c in qs]}


@register_tool
class CreateCampaign(AssistantTool):
    name = "create_marketing_campaign"
    description = "Create a marketing campaign."
    module_id = "campaigns"
    required_permission = "campaigns.add_campaign"
    requires_confirmation = True
    parameters = {
        "type": "object",
        "properties": {
            "name": {"type": "string"}, "campaign_type": {"type": "string"},
            "description": {"type": "string"}, "start_date": {"type": "string"},
            "end_date": {"type": "string"}, "budget": {"type": "string"},
        },
        "required": ["name"],
        "additionalProperties": False,
    }

    def execute(self, args, request):
        from decimal import Decimal
        from campaigns.models import Campaign
        c = Campaign.objects.create(name=args['name'], campaign_type=args.get('campaign_type', ''), description=args.get('description', ''), start_date=args.get('start_date'), end_date=args.get('end_date'), budget=Decimal(args['budget']) if args.get('budget') else None)
        return {"id": str(c.id), "name": c.name, "created": True}
