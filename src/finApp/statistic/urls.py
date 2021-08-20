from django.urls import path
from . import views

app_name = 'statistic'
urlpatterns = [
    # the name parameter can be used in django template to reference the url
    path('test/', views.testConnection),  # test view - to be deleted
    path('home/', views.showHome, name='home'),
    path('transaction/<slug:slug>',
         views.showTransaction, name='transaction'),

    # path('', views.StatisticsView.as_view(), name='statistics'),
    # path('/<int:pk>/', views.DetailView.as_view(), name='detailed'),
    # path('/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('/<int:question_id>/vote/', views.vote, name='vote'),
]
