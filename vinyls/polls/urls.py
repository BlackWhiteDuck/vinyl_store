'''Added a urls.py file within the polls app in order to create a url for each function within the views.py file, using path and 
naming the url accordingly'''

from django.urls import path, include
# imported path and include from django.urls
from . import views
# imported views from .import

app_name='polls'
# created an app name called 'polls'

urlpatterns = [
    # created a urlpatterns list 
    path('', views.index, name="index"),
    # used path to create a path to views for the index function within the views file and named it 'index'
    path('<int:question_id>/', views.detail, name='detail'),
    # used path to create a path to views for the detail function within the views file and named it 'detail' and made
    # and showed that the question_id is an integer
    path('<int:question_id>/results/', views.results, name='results'),
    # used path to create a path to views for the results function within the views file and named it 'results' and made
    # and showed that the question_id is an integer; and listed results in the url
    path('<int:question_id>/vote/', views.vote, name='vote')
     # used path to create a path to views for the vote function within the views file and named it 'vote' and made
    # and showed that the question_id is an integer; and listed votes in the url
]
