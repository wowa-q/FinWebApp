from django.contrib import admin

# Register your models here.
from .models import Creditor, Transaction, Project#, User

admin.site.register(Creditor)
admin.site.register(Transaction)
admin.site.register(Project)