from django.urls import path 
from . import views

# define the urls
urlpatterns = [
    path('customers/', views.kycs),
    path('customer/<int:pk>/', views.kyc),
]