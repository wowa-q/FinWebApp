from django.urls import path
#from django.conf.urls import url
from . import views

app_name = 'loader'
urlpatterns = [
    # the name parameter can be used in django template to reference the url

    # show statistics of the transactions
    #path('', views.transaction_list),
    path('creditors/', views.creditor_list, name='creditors'),
    path('test/', views.testConnection),
    path('transactions/', views.transactions, name='transactions'),
    path('transaction/<slug:trans_slug>',
         views.transaction, name='transaction'),

    path('transactions/', views.transactions, name='statistics'),
    path('transactions/', views.transactions, name='budget'),
    path('transactions/', views.transactions, name='settings'),
    path('transactions/', views.transactions, name='profile'),

    #path('', views.StatisticsView.as_view(), name='statistics'),
    #     path('/<int:pk>/', views.DetailView.as_view(), name='detailed'),
    #     path('/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #     path('/<int:question_id>/vote/', views.vote, name='vote'),
]
