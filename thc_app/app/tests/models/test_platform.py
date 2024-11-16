from app.const import PlatformCategory
from app.models.platform import Platform
from app.utils import generate_fake_checksum
from django.test import TestCase


class PlatformTestClass(TestCase):
    def setUp(self):
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

    def test_basic_data(self):
        platform = Platform.objects.all().first()
        self.assertEqual(platform.name, "PlayStation 9")
        self.assertEqual(platform.slug, "playstation-9")
