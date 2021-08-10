from enum import unique

from django.db import models


# Create your models here.
class Transaction(models.Model):

    # TODO: add validators for the slug
    # validators = [function 1, function 2]
    slug = models.SlugField(unique=True,
                            primary_key=True,
                            editable=False)
    # Konto
    account = models.CharField(max_length=24, default='')
    # Betrag
    value = models.CharField(max_length=10, default='')
    # verwendungszweck
    aim = models.CharField(max_length=300, default='')     #
    # Buchungstext
    textBooking = models.CharField(max_length=300, default='')
    # Auftraggeber
    customer = models.CharField(max_length=300, default='')
    blz = models.CharField(max_length=14)
    # Glaeubiger-ID
    creditorId = models.CharField(max_length=40, default='')
    # Mandatsreferenz
    mandat = models.CharField(max_length=40, default='')
    # Kundenreferenz
    customerReference = models.CharField(max_length=40, default='')
    # Transaction date
    date = models.DateTimeField()
    # Date imported
    # pub_date = models.DateTimeField(default=timezone.now)

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
        return 'Transaction model'


class Classification(models.Model):
    tag = models.CharField(max_length=40)

    def __str__(self):
        return 'Classification model'
