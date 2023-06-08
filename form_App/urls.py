from django.urls import path
from .views import *


urlpatterns = [
    path('signin_page/', signin_page, name='signin_page'),
    path('', signup_page, name='signup_page'),

    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('index/', index, name='index'),
    path('logout/', logout, name='logout'),
]