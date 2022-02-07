from cmath import log
import json
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from rest_framework.utils import serializer_helpers
from .models import Note
from .serializers import NoteSerializer
from api import serializers


@api_view(['GET'])
def getRoutes(request):

    return Response("hii there")


@api_view(['POST'])
def getFilteredNote(request):
    data = request.data
    fiternotes = NoteSerializer(Note.objects.filter(
        createdBy=data['createdBy']).order_by('-updated'), many=True)

    return Response(fiternotes.data)


@api_view(['POST'])
def getNotes(request):
    # if request.method == 'GET':
    #     notes = Note.objects.all().order_by('-updated')
    #     serializer = NoteSerializer(notes, many=True)
    #     # data = Note.objects.filter(createdBy=request.user)
    #     # serializer = NoteSerializer(data, many=True)

    #     print(serializer.data)
    #     return Response(serializer.data, status=200)

    if request.method == 'POST':
        data = request.data
        note = Note.objects.create(
            body=data['body'], createdBy=data['createdBy'])
        serializer = NoteSerializer(note, many=False)
        print(note)
        return Response(serializer.data, status=200)


@api_view(['GET', 'PUT', 'DELETE'])
def getNote(request, pk):
    if request.method == 'GET':
        notes = Note.objects.get(id=pk)
        serializer = NoteSerializer(notes, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        data = request.data
        note = Note.objects.get(id=pk)
        serializer = NoteSerializer(instance=note, data=data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    if request.method == 'DELETE':
        note = Note.objects.get(id=pk)
        note.delete()

        return Response('Note deleted!')


# @api_view(['POST'])
# def createNote(request):
#     data = request.data
#     note = Note.objects.create(body=data['body'])
#     serializer = NoteSerializer(note, many=False)
#     return Response(serializer.data)


# @api_view(['PUT'])
# def updateNote(request, pk):
#     data = request.data
#     note = Note.objects.get(id=pk)
#     serializer = NoteSerializer(instance=note, data=data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


# @api_view(['DELETE'])
# def deleteNote(request, pk):

#     note = Note.objects.get(id=pk)
#     note.delete()

#     return Response('Note was deleted!')
