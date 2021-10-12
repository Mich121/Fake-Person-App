from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .views import UserCreate, registration_view, logout_view

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register1/', UserCreate.as_view(), name='register1'),
    path('register2/', registration_view, name='register2'),
    path('logout/', logout_view, name='logout'),
]