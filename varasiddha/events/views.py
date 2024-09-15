from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Event

def events(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        category = request.POST.get('category')
        Event.objects.create(name=name, date=date, category=category)
        return redirect('events')

    events = Event.objects.all()
    return render(request, 'events/events.html', {'events': events})
