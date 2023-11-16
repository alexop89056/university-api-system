from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.mixins import ListModelMixin
from api.models import Student
from api.pagination.student import StudentsListPagination
from api.serializers.student import StudentSerializer
from django.db.models import Q


# @extend_schema(
#     parameters=[
#         OpenApiParameter(
#             name='page',
#             type=OpenApiTypes.INT,
#             location=OpenApiParameter.QUERY,
#             required=False,
#             description='Get list by page'
#         ),
#         OpenApiParameter(
#             name='query',
#             type=OpenApiTypes.STR,
#             location=OpenApiParameter.QUERY,
#             required=False,
#             description='Search query body'
#         ),
#     ],
#     responses=StudentSerializer(many=True),
# )
# def get(self, request, *args, **kwargs):
#     return super().get(request, *args, **kwargs)

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
        ],
        responses=StudentSerializer(many=True)
    )
class StudentsView(ListAPIView, ListModelMixin):
    queryset = Student.objects.all().order_by('id')
    serializer_class = StudentSerializer
    pagination_class = StudentsListPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name')
        surname = self.request.query_params.get('surname')

        if name or surname:
            filter_params = Q()

            if name:
                filter_params |= Q(name__icontains=name)

            if surname:
                filter_params |= Q(surname__icontains=surname)

            queryset = queryset.filter(filter_params)

        return queryset


class StudentView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CreateStudentView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
