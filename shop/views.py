from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def archives_year(request, year):
    response = f'{year}년도에 대한 내용'
# response['key'] = 'value'
    return response
    #return HttpResponse('{}년도에 대한 내용'.format(year))
