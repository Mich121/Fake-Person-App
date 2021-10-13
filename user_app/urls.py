from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .views import UserCreate, registration_view, logout_view, login_view, registration_JWT_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    #path('login1/', obtain_auth_token, name='login'), #or
    path('login1/', login_view, name='login'),
    path('logout1/', logout_view, name='logout'),
    path('register1/', registration_view, name='register1'),

    #path('register2/', UserCreate.as_view(), name='register2'),
    
    #using JWT authentication
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('register3/', registration_JWT_view, name='register3'),

    
]