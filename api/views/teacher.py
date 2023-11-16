from django.db.models import Q
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.mixins import ListModelMixin

from api.models import Teacher
from api.pagination.teacher import TeachersPagination
from api.serializers.teacher import TeacherSerializer


@extend_schema(
        parameters=[
            OpenApiParameter(
                name='name',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                required=False,
                description='Name field for searching'
            ),
            OpenApiParameter(
                name='surname',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                required=False,
                description='Surname field for searching'
            ),
            OpenApiParameter(
                name='rank',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                required=False,
                description='Rank field for searching'
            ),
        ],
        responses=TeacherSerializer(many=True)
    )
class TeachersView(ListAPIView, ListModelMixin):
    queryset = Teacher.objects.all().order_by('id')
    serializer_class = TeacherSerializer
    pagination_class = TeachersPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name')
        surname = self.request.query_params.get('surname')
        rank = self.request.query_params.get('rank')

        if name or surname or rank:
            filter_params = Q()

            if name:
                filter_params |= Q(name__icontains=name)

            if surname:
                filter_params |= Q(surname__icontains=surname)

            if rank:
                filter_params |= Q(rank__icontains=rank)

            queryset = queryset.filter(filter_params)
        return queryset


class TeacherView(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class CreateTeacherView(CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
