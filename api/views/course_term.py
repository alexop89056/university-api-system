from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.mixins import ListModelMixin

from api.models import CourseTerm
from api.pagination.course_term import CourseTermsPagination
from api.serializers.course_term import CourseTermSerializer


class CourseTermsView(ListAPIView, ListModelMixin):
    queryset = CourseTerm.objects.all().order_by('id')
    serializer_class = CourseTermSerializer
    pagination_class = CourseTermsPagination


class CourseTermView(RetrieveUpdateDestroyAPIView):
    queryset = CourseTerm.objects.all()
    serializer_class = CourseTermSerializer


class CreateCourseTermView(CreateAPIView):
    queryset = CourseTerm.objects.all()
    serializer_class = CourseTermSerializer
