from ninja import NinjaAPI
from .game import game_api
from .user import user_api
from .test import test


ninja_api = NinjaAPI()

# Add routers to the API
ninja_api.add_router("/game", game_api)
ninja_api.add_router("/user", user_api)
ninja_api.add_router("/test", test)
