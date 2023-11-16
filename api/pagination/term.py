from rest_framework.pagination import PageNumberPagination


class TermsListPagination(PageNumberPagination):
    page_size = 5