from rest_framework.pagination import PageNumberPagination


class CoursesListPagination(PageNumberPagination):
    page_size = 5