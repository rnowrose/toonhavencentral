from app.models.tenants import Client
from django.core.management.base import BaseCommand
from django.forms import ValidationError
from django_tenants.utils import schema_context

class Command(BaseCommand):
    help = "Create a new tenant"

    print("Loading create_tenant management command")

    def add_arguments(self, parser):
        parser.add_argument("schema_name", type=str, help="Schema name")
        parser.add_argument("name", type=str, help="Tenant name")

    def handle(self, **options):
        schema_name = options.get("schema_name")
        name = options.get("name")
        
        with schema_context('public'):
            if Client.objects.filter(schema_name=schema_name).exists():
                self.stdout.write(
                    self.style.ERROR(
                        f"Tenant with schema '{schema_name}' already exists."
                    )
                )
                return

            tenant = Client(schema_name=schema_name, name=name)
            try:
                tenant.full_clean()  # Validate before saving
                tenant.save()  # Save the tenant to the database
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