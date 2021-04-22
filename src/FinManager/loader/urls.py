from django.urls import path
#from django.conf.urls import url
from . import views

app_name = 'loader'
urlpatterns = [
    # show statistics of the transactions     
    path('', views.StatisticsView.as_view(), name='statistics'),
#     path('/<int:pk>/', views.DetailView.as_view(), name='detailed'),
#     path('/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#     path('/<int:question_id>/vote/', views.vote, name='vote'),
]