
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.urls import reverse
from django.utils import timezone

from .models import Project, Transaction, Creditor

# Create your views here.
class TransactionView(generic.DetailView):
    #TODO: update view to show the statistics of the transactions
    model = Transaction
    template_name = 'loader/statistics.html'
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Transaction.objects.filter(pub_date__lte=timezone.now())
    
class StatisticsView(generic.ListView):
    #TODO: update view to show the statistics of the transactions
    model = Transaction
    template_name = 'loader/statistics.html'
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Transaction.objects.filter(pub_date__lte=timezone.now())