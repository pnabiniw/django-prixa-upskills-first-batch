from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class CustomPagination(LimitOffsetPagination):
    def get_paginated_response(self, data):
        return Response({
            'totalData': self.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'data': data
        })
