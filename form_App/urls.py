from django.urls import path
from .views import *


urlpatterns = [
    path('signin_page/', signin_page, name='signin_page'),
    path('signup_page/', signup_page, name='signup_page'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('profile_page/', profile_page, name='profile_page'),


    path('', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('index/', index, name='index'),
    path('logout/', logout, name='logout'),
    path('profile_update/', profile_update, name='profile_update'),
    path('profile_data/', profile_data, name='profile_data'),
    path('delete_account_function/',delete_account_function,name='delete_account_function'),
]