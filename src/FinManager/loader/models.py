# Create your models here.
import datetime
from django.db import models
from django.utils import timezone


class Project(models.Model):
    title = models.CharField(max_length=60)
    nrTransactions = models.IntegerField(default=0)
    firstTransact = models.DateTimeField(default=timezone.now)
    lastTransact = models.DateTimeField(default=timezone.now)
    dateCreated = models.DateTimeField(default=timezone.now)
    dateUpdated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Project'


class Creditor(models.Model):
    nameCredior = models.CharField(max_length=60)
    counter = models.IntegerField(default=0)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def unique(self, list1):
        # intilize a null list
        unique_list = []
        # traverse for all elements
        for x in list1:
            # check if exists in unique_list or not
            if x not in unique_list:
                unique_list.append(x)

        # np.unique() needs to be installed first to use

    def __str__(self):
        return 'Creditor'


class Transaction(models.Model):
    # https://docs.djangoproject.com/en/3.2/howto/custom-model-fields/
    # https://docs.djangoproject.com/en/3.2/ref/models/fields/#autofield
    # TODO: make auto calculated
    account = models.CharField(max_length=24, default='')  # Konto
    value = models.CharField(max_length=10, default='')
    creditor = models.ForeignKey(Creditor, on_delete=models.CASCADE)
    verwendungszweck = models.CharField(max_length=300, default='')
    textBooking = models.CharField(max_length=300, default='')  # Buchungstext
    customer = models.CharField(max_length=300, default='')  # Auftraggeber
    #BLZ = models.CharField(max_length=14)
    creditorId = models.CharField(max_length=40, default='')  # Glaeubiger-ID
    mandat = models.CharField(max_length=40, default='')  # Mandatsreferenz
    customerReference = models.CharField(
        max_length=40, default='')  # Kundenreferenz
    category = models.CharField(max_length=40, default='')
    # TODO: choose the right field
    types = models.CharField(max_length=40, default='')
    # TODO: choose the right field
    tags = models.CharField(max_length=40, default='')
    pub_date = models.DateTimeField(default=timezone.now)
    """
    #direction           = models.BooleanField()  #TODO: choose type
    id_commulated       = str(ID)+str(pub_date)
    def was_received(self):
        return self.value > 0             
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    """

    def __str__(self):
        return 'Transaction'
