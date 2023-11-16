from rest_framework.pagination import PageNumberPagination


class TeachersPagination(PageNumberPagination):
    page_size = 10