from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size=10
    page_query_param='p'
    page_size_query_param='show' # user can define number of records in a page
    # max_page_size=10
    # last_page_strings='end'


class MyLOP(LimitOffsetPagination):
    default_limit=5
    limit_query_param='l'
    offset_query_param='os'
    # max_limit=6