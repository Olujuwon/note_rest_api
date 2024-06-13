from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Note


class NoteTestCase(APITestCase):

    def test_create_note(self):
        url = reverse('notes')
        data = {'owner': '1', 'body': 'test body'}
        response = self.client.post(url, data)
        print("test_create_note", response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 1)

    def test_get_notes(self):
        url = reverse('notes')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
