from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    # my account
    path('dashboard/', views.dashboard, name='dashboard'),
    path('my_orders/',  views.my_orders, name='my_orders'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),

    # forget password
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('resetpassword_validate/<uidb64>/<token>/',
         views.reset_password_validate, name='resetpassword_validate'),
    path('reset_password/', views.reset_password,
         name='reset_password'),
]
