'''
@author: wakl8754
@purpose: implementation of django models for the App: finApp
'''
from django.db import models


class Classification(models.Model):
    '''
        Model to classify the transactions
    '''
    klasse = models.CharField(max_length=40)

    def __str__(self):
        return f'Class: {self.klasse}'


class Category(models.Model):
    '''
        Model for transaction categories
    '''
    category = models.CharField(max_length=40)

    def __str__(self):
        return f'Category: {self.category}'


class Tags(models.Model):
    '''
        Model for transaction tags
    '''
    tag = models.CharField(max_length=40)

    def __str__(self):
        return f'Tag: {self.tag}'


class Transaction(models.Model):
    ''' Transaction model'''
    # TODO: add validators for the slug
    # validators = [function 1, function 2]

    slug = models.SlugField(unique=True)
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
    # ForeignKey: one to many relation
    classification = models.ForeignKey(
        Classification, blank=True, null=True, on_delete=models.CASCADE)
    cathegory = models.ForeignKey(
        Category, blank=True, null=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(
        Tags, blank=True, null=True)

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
        return f'Transaction slug: {self.slug}'
