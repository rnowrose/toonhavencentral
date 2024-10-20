from django.core.management.base import BaseCommand
from django.forms import ValidationError

from app.models.tenants import Client
from django_tenants.utils import schema_context


class Command(BaseCommand):
    help = 'Create a new tenant'

    def add_arguments(self, parser):
        parser.add_argument("schema_name", type=str, help="Schema name")
        parser.add_argument('name', type=str, help='Tenant name')

    def handle(self, *args, **options):
        schema_name = options['schema']
        name = options['name']
        with schema_context(schema_name):
            if Client.objects.filter(schema_name=schema_name).exists():
                self.stdout.write(
                    self.style.ERROR(
                        f"Tenant with schema '{schema_name}' already exists."
                    )
                )
                return

            # Create the tenant
            tenant = Client(schema_name=schema_name, name=name)

            try:
                tenant.full_clean()  # Validate the model before saving
                tenant.save()
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Tenant '{name}' with schema '{schema_name}' created successfully!"
                    )
                )
            except ValidationError as e:
                self.stdout.write(
                    self.style.ERROR(f"Error creating tenant: {', '.join(e.messages)}")
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"An unexpected error occurred: {str(e)}")
                )
