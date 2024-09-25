from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Donation
from django.http import FileResponse
import os
from django.conf import settings
import logging

def download_donation_info(request):
    if request.user.is_authenticated:
        logger.info(f"User {request.user.username} downloaded the donation info.")
    else:
        logger.info("An anonymous user downloaded the donation info.")
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
