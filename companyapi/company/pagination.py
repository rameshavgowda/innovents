from rest_framework.pagination import PageNumberPagination

class MypagePagination(PageNumberPagination):
    page_size=3
    page_query_param= 'p'
