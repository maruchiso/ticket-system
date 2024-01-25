from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from .models import Zgloszenie
from .forms import ZgloszenieForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if user.role == 'admin':
                    return redirect('admin_dashboard')
                else:
                    return redirect('user_dashboard')
    
    else:
        form = LoginForm()

    return render(request, 'login/login.html', {'form': form})

@login_required
def panel_uzytkownika(request):
    username = request.user.username
    zgloszenia = Zgloszenie.objects.filter(submitted_by=request.user)

    if request.method == 'POST':
        form = ZgloszenieForm(request.POST)
        if form.is_valid():
            zgloszenie = form.save(commit=False)
            zgloszenie.submitted_by = request.user
            zgloszenie.save()
            return redirect('panel_uzytkownika')
    else:
        form = ZgloszenieForm()
    
    return render(request, 'login/panel_uzytkownika.html', {'username': username, 'zgloszenia': zgloszenia, 'form': form})
