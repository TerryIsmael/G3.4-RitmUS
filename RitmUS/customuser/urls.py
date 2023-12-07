from django.urls import path
from .views import register,custom_login, create_incidence, list_incidences,change_user,change_password

urlpatterns = [
    path('register/', register, name='register'),
    path('user/login/', custom_login, name='custom_login'),
    path('incidence/new/', create_incidence, name='create_incidence'),
    path('incidence/list/', list_incidences, name='list_incidences'),
    path('user/my_account', change_user, name='change_user'),
    path('user/my_account/change_password', change_password, name='change_password'),
]