from django.shortcuts import render
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data()
    form = RegistrationForm()
    return render(request,'accounts/register.html')

def login(request):
    return render(request,'accounts/login.html')


def logout(request):
    return 