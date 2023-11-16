from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.mixins import ListModelMixin

from api.models import StudentCard
from api.pagination.student_card import StudentCardsPagination
from api.serializers.student_card import StudentCardSerializer


class StudentCardsView(ListAPIView, ListModelMixin):
    queryset = StudentCard.objects.all().order_by('id')
    serializer_class = StudentCardSerializer
    pagination_class = StudentCardsPagination


class StudentCardView(RetrieveUpdateDestroyAPIView):
    queryset = StudentCard.objects.all()
    serializer_class = StudentCardSerializer


class CreateStudentCardView(CreateAPIView):
    queryset = StudentCard.objects.all()
    serializer_class = StudentCardSerializer