from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    '''Домашняя страница'''

    return HttpResponse('<html><title>To-Do lists</title></html>')
