# Create your models here.
from django.utils import timezone
from django.db import models
import datetime
#import numpy as np


class Creditor(models.Model):
    '''
    # insert the list to the set
    list_set = set(list1)
    # convert the set to the list
    unique_list = (list(list_set))
    '''
    creditorID          = models.IntegerField(default=0)  #TODO: make auto calculated
    creditorName        = models.CharField(max_length=60)
    transactionCtr      = models.IntegerField(default=0)
    
    #project             = models.ForeignKey(Project, on_delete=models.CASCADE)
    #transactions        = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    
    def unique(self, list1): 
        # intilize a null list
        unique_list = []         
        # traverse for all elements
        for x in list1:
            # check if exists in unique_list or not
            if x not in unique_list:
                unique_list.append(x)
        
        #np.unique() needs to be installed first to use
        
    def __str__(self):
        return self.nacreditorNameme
 
class Transaction(models.Model):
#https://docs.djangoproject.com/en/3.2/howto/custom-model-fields/
#https://docs.djangoproject.com/en/3.2/ref/models/fields/#autofield
    transactionID       = models.IntegerField(default=0)  #TODO: make auto calculated    
    account             = models.CharField(max_length=24) # Konto
    """
    #direction           = models.BooleanField()  #TODO: choose type
    pub_date            = models.DateTimeField('date transacted')
    id_commulated       = str(ID)+str(pub_date)
    creditor            = models.ForeignKey(Creditor, on_delete=models.CASCADE)
    
    value               = models.CharField(max_length=10)
    verwendungszweck    = models.CharField(max_length=300) 
    textBooking         = models.CharField(max_length=300) # Buchungstext
    customer            = models.CharField(max_length=300) # Auftraggeber
    BLZ                 = models.CharField(max_length=14)
    creditorId          = models.CharField(max_length=40) # Glaeubiger-ID
    mandat              = models.CharField(max_length=40) # Mandatsreferenz
    customerReference   = models.CharField(max_length=40) # Kundenreferenz
    
    category            = models.CharField(max_length=40)
    types               = models.CharField(max_length=40) #TODO: choose the right field
    tags                = models.CharField(max_length=40) #TODO: choose the right field    
    
    def was_received(self):
        return self.value > 0             
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    def __str__(self):
        return [self.ID, self.value, self.date]
"""

class Project(models.Model):
    pjName            = models.CharField(max_length=60)
    """
    nrTransactions  = models.IntegerField(default=0)
    firstTransact   = models.DateTimeField('pub_date')
    lastTransact    = models.DateTimeField('pub_date')
    dateCreated     = models.DateTimeField('pub_date')
    dateUpdated     = models.DateTimeField('pub_date')
    transactions    = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    
    def update(self):
        '''
        update transaction properties view
        '''
        pass
    """