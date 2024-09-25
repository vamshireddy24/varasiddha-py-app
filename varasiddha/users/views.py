# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib import messages
from django.http import FileResponse, Http404, HttpResponseNotAllowed
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    
def index(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    current_datetime = datetime.now()
    return render(request, 'index.html', {'current_datetime': current_datetime})
def about(request):
    # Only allow GET requests for this view
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    return render(request, 'about.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dharshana')
    elif request.method == 'GET':
        form = AuthenticationForm()
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])  # Disallow other methods
    return render(request, 'users/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # Load the profile instance created by the signal
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            form.save()
            return redirect('login')
    elif request.method == 'GET':
        form = CustomUserCreationForm()
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])  # Disallow other methods
    return render(request, 'users/register.html', {'form': form})

def user_logout(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    logout(request)
    return redirect('index')
