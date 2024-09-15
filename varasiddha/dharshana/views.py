from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Dharshana
from django.contrib.auth.views import LoginView

@login_required
def dharshana(request):
    prices = Dharshana.objects.all()
    return render(request, 'dharshana/dharshana.html', {'prices': prices})

class CustomLoginView(LoginView):
    template_name = 'users/login.html'