from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.accounts.views import (UserLoginView, UserProfileView, UserRegistrationView)

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]