from django.test import TestCase
from app.models.games import Game
from app.utils import generate_fake_checksum
from app.models.platform import Platform
from app.const import PlatformCategory

class GameTestClass(TestCase):
    DUMMY_ID=100000

    def setUp(self):
        g1 = Game.objects.create(
            name="Game 1",
            slug="game-1",
            summary="This guy jumped from abuilding",
            storyline='This is a story of some cat',
            checksum=generate_fake_checksum('game 1'),
        )
        
        g2 = Game.objects.create(
            name="Game 2",
            slug="game-2",
            summary="This guy jumped from abuilding",
            checksum=generate_fake_checksum('game 1'),
        )
        
        p1 = Platform.objects.create(
            name="PlayStation 9",
            abbreviation="PS9",
            alternative_name="PS9",
            category=PlatformCategory.CONSOLE,
            generation=9,
            slug="playstation-9",
            summary="this is good",
            url="www.ps9.com",
            checksum=generate_fake_checksum("game 1"),
        )

    def test_get_all_data(self):
        game_list = []
        games = Game.objects.all()
        for game in games:
            game_list.append(game.name)
        
        self.assertEqual(game_list, ['Game 1', 'Game 2'])
        
    
    def test_basic_properies(self):
        g = Game.objects.all().first()
        self.assertEqual(g.name, "Game 1")
        self.assertEqual(g.slug, "game-1")
        self.assertEqual(g.storyline, "This is a story of some cat")
        
