# -- coding:utf-8 --
# --auther = summer--
from django.http import HttpResponse


def index_view(request):
    return HttpResponse('hello git!')