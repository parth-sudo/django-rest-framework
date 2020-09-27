from .models import Course
from .serializers import CourseSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

from rest_framework import mixins,generics,viewsets
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class CoursePagination(PageNumberPagination):
    page_size = 2

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CoursePagination



