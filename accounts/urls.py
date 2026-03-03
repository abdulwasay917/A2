from django.urls import path
from .views import signup, user_login, forgot_password,user_logout,dashboard,reset_password,EditView,verify_email,profile_view

urlpatterns = [
    path('login/', user_login, name='login'),
    path('signup/', signup, name='signup'),
    path('forgot-password/', forgot_password, name='forgot_password'),
    path('logout/', user_logout, name='logout'),
    path('profile/edit/<int:pk>/', EditView.as_view() , name='edit'),
    path('profile/view/', profile_view, name='view'),
    path('dashboard/',dashboard , name='dashboard'),
    path('reset-password/<uidb64>/<token>/', reset_password, name='reset_password'),
    path('verify-email/<uidb64>/<token>/', verify_email, name='verify_email'),
]

