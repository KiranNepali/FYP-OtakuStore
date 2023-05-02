from django.urls import path
from . import views


urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),
    path('payments/', views.payments, name='payments'),
    # path('khalti_verify/',
    #      views.KhaltiVerify, name='khalti_verify'),

]
