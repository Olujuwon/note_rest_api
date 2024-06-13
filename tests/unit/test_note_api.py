from django.test import TestCase
from api.serializers import NoteSerializer


class NoteUnitTestCase(TestCase):
    def test_valid_serializer_data(self):
        data = {'owner': '1', 'body': 'test body'}
        serialized_data = NoteSerializer(data=data)
        print("Serialized for correct data",serialized_data.is_valid())
        self.assertTrue(serialized_data.is_valid())

    def test_not_valid_serializer_data(self):
        data = {'body': 'test body'}
        serialized_data = NoteSerializer(data=data)
        self.assertFalse(serialized_data.is_valid())
