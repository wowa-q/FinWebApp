from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request


# temporary list to be used instead of DB data
transactions_list = [
    {'date': '20.05.2020',
     'slug': 'first-trans',
     'value': 10,
     'target': 'Beguenstigter',
     'aim': 'nado'
     },
    {'date': '21.05.2020',
     'slug': 'second-trans',
     'value': 20,
     'target': 'Beguenstigter',
     'aim': 'nado'
     }
]

# Create your views here.


def testConnection(request):
    return HttpResponse('This is connection test')


def showHome(request):
    # view to the main home page
    return render(request, 'statistic/home.html', {'transaction': transactions_list})


def showTransaction(request, slug):
    # view to show a single transaction
    return render(request, 'statistic/transaction.html', {'transaction': transactions_list})
