from django.urls import path
from .views import home, user_registration, user_profile

urlpatterns = [
    path('', home, name='home'),
    path('user-registration', user_registration, name='user_registration'),
    path('user-profile', user_profile, name='user_profile')
]
