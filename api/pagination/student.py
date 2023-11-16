from rest_framework.pagination import PageNumberPagination


class StudentsListPagination(PageNumberPagination):
    page_size = 3