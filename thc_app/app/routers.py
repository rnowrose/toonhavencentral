class MultiSchemaRouter:
    # Map app labels to specific schemas
    django_maps = {
        "auth": "admin",  # Maps the 'auth' app to the 'admin' schema
        "admin": "admin",  # Maps the 'admin' app to the 'admin' schema
        "contenttypes": "admin",  # Maps the 'contenttypes' app to the 'admin' schema
        "sessions": "admin",  # Maps the 'sessions' app to the 'admin' schema
        "messages": "admin",  # Maps the 'messages' app to the 'admin' schema
        "sites": "admin",  # Maps the 'sites' app to the 'admin' schema
        "migrations": "admin",  # Maps the 'migrations' app to the 'admin' schema
        "app" : "games"
        # Add more mappings for other apps as needed
    }

    model_to_schema = {
        "platform": "games",  
    }

    def db_for_read(self, model, **hints):
        """
        Direct read operations to the appropriate schema based on the model's app label or specific model mapping.
        """
        model_name = f"{model._meta.app_label}.{model.__name__}"
        schema = self.model_to_schema.get(model_name) or self.django_maps.get(
            model._meta.app_label, "public"
        )
        return schema

    def db_for_write(self, model, **hints):
        """
        Direct write operations to the appropriate schema based on the model's app label or specific model mapping.
        """
        model_name = f"{model._meta.app_label}.{model.__name__}"
        schema = self.model_to_schema.get(model_name) or self.django_maps.get(
            model._meta.app_label, "public"
        )
        return schema

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Controls which schema should handle migrations based on the model's app label or specific model mapping.
        """
        model_name_full = f"{app_label}.{model_name}" if model_name else app_label
        return self.model_to_schema.get(model_name_full) or self.django_maps.get(
            app_label, "public"
        )
