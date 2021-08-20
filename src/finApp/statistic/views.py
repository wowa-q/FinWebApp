'''
@author: wakl8754
@purpose: implementation of django views for the App: finApp
'''
from django.http import HttpResponse
from django.shortcuts import render
from .models import Transaction

# Create your views here.


def test_connection(request):
    '''
        test view - nothing to be done with it
    '''
    print(request)
    return HttpResponse('This is connection test')


def show_home(request):
    '''
     view to the main home page
    '''
    context = {
        'transactions': Transaction.objects.all()
    }
    return render(request, 'statistic/home.html', context)


def show_transaction(request, slug):
    '''
    view to show a selected transaction
    '''
    transaction = Transaction.objects.get(slug=slug)
    print(transaction)
    return render(request, 'statistic/transaction.html', {'transaction': transaction})
