'''
@author: wakl8754
@purpose: implementation of admin interface models for the App: finApp
'''
from django.contrib import admin
from .models import Transaction, Classification, Tags, Category
# Register your models here.
admin.site.register(Transaction)
admin.site.register(Classification)
admin.site.register(Tags)
admin.site.register(Category)
