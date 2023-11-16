from rest_framework.pagination import PageNumberPagination


class CourseTermsPagination(PageNumberPagination):
    page_size = 3