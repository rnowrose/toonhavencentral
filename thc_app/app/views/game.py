from ninja import NinjaAPI, Router


game_api = Router()

@game_api.get("/api-example")
def example_view(request):
    return {"message": "Hello, Ninja API!"}

