from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('', views.dharshana, name='dharshana'),
    path('login/', CustomLoginView.as_view(), name='login'),
]
