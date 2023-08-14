'''Added a urls.py file within the mainpage app in order to create a url for each function within the views.py file, using path and 
naming the url accordingly'''

from django.urls import path
# imported path from django.urls
from . import views
# imported views from .

urlpatterns = [
    path('', views.main, name='main'),
    path('user_info/', views.user_info, name='user_info')
]
# created a urlpatterns list, and created paths for the main function, and the user_info function;
# named them all