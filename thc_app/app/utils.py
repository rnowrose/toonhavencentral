from django.core.management import call_command
from django_tenants.utils import get_tenant_model


def migrate_tenants():
    Tenant = get_tenant_model()
    tenants = Tenant.objects.all()

    for tenant in tenants:
        call_command("migrate", schema=tenant.schema_name)
