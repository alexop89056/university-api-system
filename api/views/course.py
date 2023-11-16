from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.mixins import ListModelMixin

from api.models import Course
from api.pagination.course import CoursesListPagination
from api.serializers.course import CourseSerializer


class CoursesView(ListAPIView, ListModelMixin):
    queryset = Course.objects.all().order_by('id')
    serializer_class = CourseSerializer
    pagination_class = CoursesListPagination


class CourseView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CreateCourseView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
