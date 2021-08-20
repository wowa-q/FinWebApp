from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request
from .models import Transaction

# Create your views here.


def testConnection(request):
    return HttpResponse('This is connection test')


def showHome(request):
    # view to the main home page
    transactions = Transaction.objects.all()
    context = {
        'transactions': Transaction.objects.all()
    }
    return render(request, 'statistic/home.html', context)


def showTransaction(request, slug):
    transaction = Transaction.objects.get(slug=slug)
    print(transaction)
    return render(request, 'statistic/transaction.html', {'transaction': transaction})
