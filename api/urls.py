from django.urls import path, include
from rest_framework import routers
from .views import Home, PersonCreate, PersonListAPI, PersonDetailAPI, PersonVS, PersonOnlineListAPI
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('person_api', PersonVS, basename='person_vs')

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('person_create/', PersonCreate.as_view(), name='person_create'),

    ###instead of this two lines we can use routers, it is viewsets only to read, you cant update, delete
    path('person_list_api/', PersonListAPI.as_view(), name='person_list_api'),
    path('person_detail_api/<int:pk>/', PersonDetailAPI.as_view(), name='person_detail_api'),
    #
    path('', include(router.urls)),
    #
    path('person_online_list_api/<int:pk>/', PersonOnlineListAPI.as_view(), name='person_online_list_api'),
    
]
