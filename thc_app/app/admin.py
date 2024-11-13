from django.contrib import admin
from app.models.games import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    model = Game
    extra = 0
    list_display = ("name", "slug", "url")
    search_fields = ('name',)
    ordering = ('name',)  # You will customize this later
