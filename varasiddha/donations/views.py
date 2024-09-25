from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Donation
from django.http import FileResponse, HttpResponseForbidden
import os
from django.conf import settings

def download_donation_info(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("You must be logged in to download this file.")
    file_path = os.path.join(settings.STATIC_ROOT, 'pdfs', 'donations.pdf')
    return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
def donations(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        Donation.objects.create(name=name, amount=amount, date=date)
        return redirect('donations')
    
    filter_by = request.GET.get('filter', '')
    donations = Donation.objects.filter(name__icontains=filter_by)
    return render(request, 'donations/donations.html', {'donations': donations})
