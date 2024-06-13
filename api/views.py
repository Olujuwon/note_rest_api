from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer
from django.views.decorators.cache import cache_page


@cache_page(60 * 5)
@api_view(['GET'])
def get_routes_info(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note - cached'
        },
        {
            'Endpoint': '/notes/',
            'method': 'POST',
            'body': {'body': {}},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'PUT',
            'body': {'body': {}},
            'description': 'Updates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an exiting note'
        },
    ]
    return Response(routes)


@cache_page(60 * 5)
@api_view(['GET', 'POST'])
def note_list_and_create(request):
    if request.method == 'GET':
        notes = Note.objects.all()
        serialized_notes = NoteSerializer(notes, many=True)
        return Response(serialized_notes.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        print('Request data', request.data)
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
