from django.test import TestCase
from django.contrib.auth.models import User


class UserTestUnitCases(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser', email='email@testuser.fi', password='VerySecuredPass24')

    def test_user_has_fields(self):
        self.assertEqual(self.user.email, 'email@testuser.fi')
        self.assertEqual(self.user.username, 'testuser')
