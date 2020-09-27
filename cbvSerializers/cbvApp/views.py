from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404


class student_list(APIView):
    def get(self,request):
        student = Student.objects.all()
        serialize=StudentSerializer(student, many=True)
        return Response(serialize.data)

    def post(self, request):
        serialize = StudentSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status.HTTP_201_CREATED)
        return Response(serialize.errors, status.HTTP_400_BAD_REQUEST)


class student_detail(APIView):
    def get_object(self,pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk):  #will return a student.
        student = self.get_object(pk)
        serialize = StudentSerializer(student)
        return Response(serialize.data)

    def put(self, request, pk): #will update student info.
        student = self.get_object(pk)
        serialize = StudentSerializer(student, request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_202_ACCEPTED)
        return Response(serialize.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk): #will delete student entry.
        student=self.get_object(pk)
        student.delete()
        return Response(status.HTTP_204_NO_CONTENT)


