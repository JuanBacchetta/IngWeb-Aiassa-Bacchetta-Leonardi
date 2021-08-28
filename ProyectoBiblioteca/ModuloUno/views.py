from django.contrib.messages.api import success
from django.http import request
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
# Create your views here.

def home(request):
    return render(request,'home.html')

@login_required(login_url='/accounts/login')
def categoria(request):
    return render(request,'categoria.html')

def registro(request):
    data = {
        'form':CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data = request.POST)
        if formulario.is_valid():
                formulario.save()
                user = authenticate(username=formulario.cleaned_data["username"],password = formulario.cleaned_data["password1"])
                login(request,user)
                return redirect(to = 'home')
        data["form"] = formulario  
    return render(request,'registration/registro.html',data)