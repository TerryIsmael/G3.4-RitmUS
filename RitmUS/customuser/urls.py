from django.urls import path
from .views import register,custom_login, create_incidence, list_incidences,change_user,change_password,request_delete_account

urlpatterns = [
    path('register/', register, name='register'),
    path('user/login/', custom_login, name='custom_login'),
    path('incidence/new/', create_incidence, name='create_incidence'),
    path('incidence/list/', list_incidences, name='list_incidences'),
    path('user/my_account', change_user, name='change_user'),
    path('user/my_account/change_password', change_password, name='change_password'),
    path('user/my_account/delete_account', request_delete_account, name='request_delete_account'),
]