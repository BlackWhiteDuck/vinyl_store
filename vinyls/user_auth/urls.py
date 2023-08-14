'''Added a urls.py file within the user_auth app in order to create a url for each function within the views.py file, using path and 
naming the url accordingly'''

from django.urls import path
# imported path from django.urls
from . import views
# imported views from .

app_name = 'user_auth'
# created an app name called 'user_auth'

urlpatterns = [
    path('', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('authenticate_user/register', views.register, name='register'),
    path('authenticate_user/show_user', views.show_user, name='show_user')
]
# created a urlpatterns list, and created paths for the user_login function, the authenticate_user function and the show_user function;
# named them all