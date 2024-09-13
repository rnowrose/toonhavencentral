import os

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": "localhost",
                "port": "5434",
                "user": "rownokn",
                "password": "rownokn",
                "database": "toonhavencentral",
            }
        }
    },
    "apps": {
        "models": {
            "models": ["app.models.auth", "app.models.pokemon",  "app.models.games", "aerich.models"],  # "app.models" should be the module where your models are defined
            "default_connection": "default",
        }
    }
}

