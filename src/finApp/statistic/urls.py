'''
@author: wakl8754
@purpose: implementation of django urls for the App: finApp
'''
from django.urls import path
from . import views

app_name = 'statistic'
urlpatterns = [
    # the name parameter can be used in django template to reference the url
    path('test/', views.test_connection),  # test view - to be deleted
    path('home/', views.show_home, name='home'),
    path('transaction/<slug:slug>',
         views.show_transaction, name='transaction'),

    # path('', views.StatisticsView.as_view(), name='statistics'),
    # path('/<int:pk>/', views.DetailView.as_view(), name='detailed'),
    # path('/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('/<int:question_id>/vote/', views.vote, name='vote'),
]
