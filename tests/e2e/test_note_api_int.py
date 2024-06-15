from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from api.models import Note


class NoteTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser', email='email@testuser.fi', password='VerySecuredPass24')
        Note.objects.create(body='Test note body', owner=self.user)
        self.client.force_authenticate(self.user)

    def test_create_note(self):
        url = reverse('notes')
        data = {'owner': '1', 'body': 'test body'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 2)

    def test_get_notes(self):
        url = reverse('notes')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_specific_note(self):
        url = reverse('notes-detail', args=(1,))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['body'], 'Test note body')

    def test_edit_specific_note(self):
        url = reverse('notes-detail', args=(1,))
        data = {'owner': '1', 'body': 'Test note body - [updated]'}
        response = self.client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['body'], 'Test note body - [updated]')

    def test_delete_specific_note(self):
        url = reverse('notes-detail', args=(1,))
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data, 'Note successfully deleted')
