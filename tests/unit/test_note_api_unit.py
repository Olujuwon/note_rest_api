from django.test import TestCase
from django.contrib.auth.models import User

from api.models import Note


class NoteTestUnitCases(TestCase):

    def setUp(self):
        new_user = User.objects.create(username='testuser', email='email@testuser.fi', password='VerySecuredPass24')
        Note.objects.create(body='Test note body', owner=new_user)

    def test_new_note_has_fields(self):
        user = User.objects.get(email='email@testuser.fi')
        note = Note.objects.get(owner=user.id)
        self.assertEqual(note.body, 'Test note body')

