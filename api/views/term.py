from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.mixins import ListModelMixin
from api.models import Term
from api.pagination.term import TermsListPagination
from api.serializers.term import TermSerializer


class TermsView(ListAPIView, ListModelMixin):
    queryset = Term.objects.all().order_by('id')
    serializer_class = TermSerializer
    pagination_class = TermsListPagination


class TermView(RetrieveUpdateDestroyAPIView):
    queryset = Term.objects.all()
    serializer_class = TermSerializer


class CreateTermView(CreateAPIView):
    queryset = Term.objects.all()
    serializer_class = TermSerializer
