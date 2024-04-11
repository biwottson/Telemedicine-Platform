from django.urls import path, include
from . import views

urlpatterns = [
    path('patient/register/', views.patient_register, name='patient_register'),
    path('provider/register/', views.provider_register, name='provider_register'),
    # Add other URL patterns for your app functionalities here
]
