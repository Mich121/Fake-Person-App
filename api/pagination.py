from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

# class PeopleListAPIPagination(PageNumberPagination):
#     page_size = 3
#     page_query_param = 'p'

# class PeopleListAPIPagination(LimitOffsetPagination):
#     default_limit = 2
#     limit_query_param = 'lim'
#     offset_query_param = 'offlim'

class PeopleListAPIPagination(CursorPagination):
    page_size = 4
    cursor_query_param = 'cur'
    ordering = 'height'
    template = 'rest_framework/pagination/numbers.html'
