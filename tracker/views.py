from django.shortcuts import render, redirect
from .models import PhishResult

def login_page(request):
    return render(request, "tracker/login.html")

def submit_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if email:
            PhishResult.objects.create(email=email)
            return redirect("/training")

    return redirect("/")

def training_page(request):
    return render(request, "tracker/training.html")
