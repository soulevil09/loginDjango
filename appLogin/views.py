from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import CadastroForm
from django.contrib.auth.views import LoginView

class HomeView(TemplateView):
    template_name = 'home.html'

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = CadastroForm()
    return render(request, 'cadastro.html', {'form': form})

class Login(LoginView):
    template_name = 'login.html' 