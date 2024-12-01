from app.utils import generate_fake_checksum
from django.test import TestCase
from django.contrib.auth.models import User

from app.models.user_profile import UserProfile


class UserTestClass(TestCase):
    def setUp(self):
        u1 = User.objects.create_user(username='username1@toonhavencentral.info', email='username1@toonhavencentral.info')
        profile = UserProfile.objects.create(user=u1, profile_name='Karim')

    def test_basic_data(self):
        user = User.objects.all().first()
        profile = UserProfile.objects.all().first()
        self.assertEqual(user.username, "username1@toonhavencentral.info")
        self.assertEqual(profile.email, "username1@toonhavencentral.info")
