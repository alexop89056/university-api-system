from rest_framework.pagination import PageNumberPagination


class StudentCardsPagination(PageNumberPagination):
    page_size = 3