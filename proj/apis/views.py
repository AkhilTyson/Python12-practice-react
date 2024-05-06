from django.shortcuts import render
from . serializers import StudentSerializer
from rest_framework.decorators import api_view
from . models import Student
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def getStud(request):
    data = Student.objects.all()
    records = StudentSerializer(data,many=True)
    return Response(records.data)

@api_view(['POST'])
def postStud(request):
    record = request.data 
    new = StudentSerializer(data = record)

    if new.is_valid():
        new.save()
        return Response(f'Successfully added {new.data}',status=200)
    return Response(new.errors,status=400)

@api_view(['PUT'])
def putStud(request):
    record = request.data 
    old = Student.objects.get(id = record['id'])
    new = StudentSerializer(old, data = record)

    if new.is_valid():
        new.save()
        return Response(f'Successfully added {new.data}',status=200)
    return Response(new.errors,status=400)

@api_view(['PATCH'])
def patchStud(request):
    record = request.data 
    old = Student.objects.get(id = record['id'])
    new = StudentSerializer(old, data = record, partial=True)

    if new.is_valid():
        new.save()
        return Response(f'Successfully added {new.data}',status=200)
    return Response(new.errors,status=400)


