# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed
from .models import Event

def events(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        category = request.POST.get('category')

        # Input validation (ensure name, date, and category are provided)
        if not name or not date or not category:
            return render(request, 'events/events.html', {
                'error': 'All fields are required.',
                'events': Event.objects.all(),
            })

        
        Event.objects.create(name=name, date=date, category=category)
        return redirect('events')
    elif request.method == 'GET':
        events = Event.objects.all()
        return render(request, 'events/events.html', {'events': events})
# Return 405 if any other method is used (e.g., PUT, DELETE)
    return HttpResponseNotAllowed(['GET', 'POST'])
