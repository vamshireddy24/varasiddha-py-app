from django.urls import path
from . import views
from .views import download_donation_info
urlpatterns = [
    path('', views.donations, name='donations'),
    path('download/', download_donation_info, name='download_donation_info'),
]
