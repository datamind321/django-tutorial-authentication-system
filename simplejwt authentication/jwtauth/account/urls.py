from django.contrib import admin
from django.urls import path , include
from account.views import UserRegistrationView,UserLoginView,UserProfileView
from account.views import *

urlpatterns = [
    path('register/', UserRegistrationView.as_view(),name='register'),
    path('login/', UserLoginView.as_view(),name='login'),
   path('view/', UserProfileView.as_view(),name='view'),
   path('changepwd/', UserChangePasswordView.as_view(),name='change_password'),
   path('resetpwd/',ChangePasswordResetEmail.as_view(),name='reset_password'),
   path('reset-password/<uid>/<token>/',UserPasswordResetView.as_view(),name='password_reset_sc'),
  

]
