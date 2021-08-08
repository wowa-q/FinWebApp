from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request


# Create your views here.
def testConnection(request):
    return HttpResponse('This is connection test')
