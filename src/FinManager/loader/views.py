
import logging

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from src.FinManager.loader import models

from .models import Project, Transaction, Creditor


logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')
# Create your views here.


def testConnection(request):
    return HttpResponse('This is connection test')


def transaction(request, trans_slug):
    transactions_list = [
        {'data': '20.05.2020',
         'slug': 'first-trans',
         'value': 10,
         'target': 'Beguenstigter',
         'aim': 'nado'
         },
        {'data': '21.05.2020',
         'slug': 'second-trans',
         'value': 20,
         'target': 'Beguenstigter',
         'aim': 'nado'
         }
    ]
    return render(request, 'loader/transaction.html', {'transaction': transactions_list})


def transactions(request):
    transactions_list = [
        {'data': '20.05.2020',
         'slug': 'first',
         'value': 10,
         'target': 'Beguenstigter',
         'aim': 'nado'
         },
        {'data': '21.05.2020',
         'slug': 'second',
         'value': 20,
         'target': 'Beguenstigter',
         'aim': 'nado'
         }
    ]
    # the dictionary can provide data which can be retrieved in the template by
    # the dictionary key
    return render(request, 'loader/home.html', {'transactions': transactions_list})


def creditor_list(request):
    creditors = Creditor.objects.all()
    transactions = Transaction.objects.all()
    context = {
        'creditors': Creditor.objects.all(),
        #'creditors': creditors,
        #'transactions': transactions
        'transactions': Transaction.objects.all()
    }
    # the function takes as first argument the request, as second the template
    # and third optional argument a dictionary. It returns a HttpResponse
    # return render(request, 'loader/statistics.html', {'creditors': creditors,
    #                                                 'transactions': transactions})
    return render(request, 'loader/statistics.html', context)


class CreditorView(generic.DetailView):
    # hier gibt man an welchem Modell gearbeitet wird
    model = Creditor()
    # hier gibt man an welches Template zu nutzen.
    # Default: <app name>/<model name>_detail.html
    template_name = 'loader/creditor_detail.html'


class TransactionView(generic.DetailView):
    # breakpoint()
    # TODO: update view to show the statistics of the transactions
    model = Transaction
    template_name = 'loader/statistics.html'
    transactions = Transaction.objects.all()
    # logging.debug(model)

    def get_queryset(self):
        '''
        Excludes any questions that aren't published yet.
        '''
        # breakpoint()
        logging.debug(Transaction.objects.filter())
        return Transaction.objects.filter()


""" """


class StatisticsView(generic.ListView):
    # TODO: update view to show the statistics of the transactions
    model = Transaction
    template_name = 'loader/statistics.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Transaction.objects.filter()
