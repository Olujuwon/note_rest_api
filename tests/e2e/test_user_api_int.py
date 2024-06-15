from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class UserAuthTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser', email='email@testuser.fi', password='VerySecuredPass24')

    """def test_user_login(self):
        url = reverse('user-login')
        print('URL', url, self.user.username)
        data = {'username': self.user.username, 'password': 'VerySecuredPass24'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #self.assertEqual(response.data['user']['email'], 'email@testuser.fi')"""

    def test_register_user(self):
        url = reverse('user_register')
        data = {'username': 'testuser01', 'password': 'VerySecuredPass24', 'email': 'email@testuser01.fi'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 2)

    def test_get_specific_user(self):
        self.client.force_authenticate(self.user)
        url = reverse('user_detail')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], 1)

    def test_user_logout(self):
        self.client.force_authenticate(self.user)
        url = reverse('knox_logoutall')
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

