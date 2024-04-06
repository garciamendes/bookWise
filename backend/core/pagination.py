from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.settings import api_settings
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size = api_settings.PAGE_SIZE
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_next_page(self):
        if not self.page.has_next():
            return None
        return self.page.next_page_number()

    def get_previous_page(self):
        if not self.page.has_previous():
            return None
        return self.page.previous_page_number()

    def get_page_size_count(self):
        return api_settings.PAGE_SIZE

    def get_pages_count(self):
        return self.page.paginator.num_pages

    def get_paginated_response(self, data):
        return Response({
            'total': self.page.paginator.count,
            'page_size': self.get_page_size_count(),
            'page_count': self.get_pages_count(),
            'current_page': self.page.number,
            'next': self.get_next_page(),
            'previous': self.get_previous_page(),
            'results': data
        })
