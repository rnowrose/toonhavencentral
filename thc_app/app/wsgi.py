"""
WSGI config for thc_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
# from django_tenants.utils import get_tenant_model, get_current_tenant


print("Python executable:", sys.executable)
print("Python version:", sys.version)
# Get the current tenant (schema)
# current_tenant = get_current_tenant()


# Access tenant-specific information
# print(current_tenant.schema_name)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

application = get_wsgi_application()
