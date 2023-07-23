from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='api_index'),
    path('register',views.registration_view,name='api_register'),
    path('login',obtain_auth_token,name='api_login'),
]