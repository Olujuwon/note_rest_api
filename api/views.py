from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes

from api_auth.serializers import UserSerializer
from .models import Note
from .serializers import NoteSerializer
from django.views.decorators.cache import cache_page
from knox.models import AuthToken


@cache_page(60 * 5)
@api_view(['GET'])
@permission_classes([AllowAny])
def get_routes_info(request):
    routes = [
        {
            'Endpoint': 'api/v1/notes',
            'method': 'GET',
            'body': None,
            'description': 'Returns array of notes',
            'status code': '200'
        },
        {
            'Endpoint': 'api/v1/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note',
            'status code': '200'
        },
        {
            'Endpoint': 'api/v1/notes',
            'method': 'POST',
            'body': {},
            'description': 'Creates new note with data sent in post request',
            'status code': '201'
        },
        {
            'Endpoint': 'api/v1/notes/id',
            'method': 'PUT',
            'body': {},
            'description': 'Updates an existing note with data sent in post request',
            'status code': '200'
        },
        {
            'Endpoint': 'api/v1/notes/id',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an exiting note',
            'status code': '204'
        },
        {
            'Endpoint': 'api/v1/auth/login',
            'method': 'POST',
            'body': {'username': '', 'password': ''},
            'description': 'Returns user data + Authorize token',
            'status code': '200'
        },
        {
            'Endpoint': 'api/v1/auth/logout',
            'method': 'POST',
            'body': None,
            'description': 'Return HTTP 204 and deletes user token',
            'status code': '204'
        },
        {
            'Endpoint': 'api/v1/auth/logoutall',
            'method': 'POST',
            'body': None,
            'description': 'Return HTTP 204 and deletes all associated user tokens',
            'status code': '204'
        },
        {
            'Endpoint': 'api/v1/auth/register',
            'method': 'POST',
            'body': {'username': '', 'password': '', 'email': ''},
            'description': 'Returns user data + Authorize token',
            'status code': '201'
        },
        {
            'Endpoint': 'api/v1/auth/user',
            'method': 'GET',
            'body': None,
            'description': 'Requires token authorization header, returns authenticated user detail',
            'status code': '200'
        },
    ]
    return Response(routes)


@cache_page(60 * 5)
@api_view(['GET', 'POST'])
def note_list_and_create(request):
    if request.method == 'GET':
        user_id = request.user.id
        notes = Note.objects.all()
        serialized_notes = NoteSerializer(notes, many=True)
        filtered_notes = [note for note in serialized_notes.data if note['owner'] == user_id]
        return Response(filtered_notes, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serialized_note = NoteSerializer(data=request.data)
        if serialized_note.is_valid():
            serialized_note.save()
            return Response(serialized_note.data, status=status.HTTP_201_CREATED)
        return Response(serialized_note.errors, status=status.HTTP_400_BAD_REQUEST)


@cache_page(60 * 5)
@api_view(['GET', 'PUT', 'DELETE'])
def note_detail_update_and_delete(request, pk):
    if request.method == 'GET':
        note = Note.objects.get(pk=pk)
        serialized_note = NoteSerializer(note)
        return Response(serialized_note.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        note = Note.objects.get(pk=pk)
        serialized_note = NoteSerializer(instance=note, data=request.data)
        if serialized_note.is_valid():
            serialized_note.save()
            return Response(serialized_note.data, status=status.HTTP_200_OK)
        return Response(serialized_note.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        note = Note.objects.get(pk=pk)
        note.delete()
        return Response('Note successfully deleted', status=status.HTTP_204_NO_CONTENT)
