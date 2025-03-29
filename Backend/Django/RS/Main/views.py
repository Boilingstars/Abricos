from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout

@login_required
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)  # Разлогиниваем пользователя
    return redirect('login')

@login_required
def auth(request):
    data = {} # Словарь data передаем функцией render()
    return render(request, 'auth.html')

@login_required
def index(request):
    data = {} # Словарь data передаем функцией render()
    return render(request, 'index.html')

@login_required
def projects(request):
    data = {} # Словарь data передаем функцией render()
    return render(request, 'index.html')

@login_required
def projects_by_slug(request):
    data = {} # Словарь data передаем функцией render()
    return render(request, 'index.html')

@login_required
def analytics(request):
    data = {} # Словарь data передаем функцией render()
    return render(request, 'index.html')

@login_required
def users(request):
    data = {} # Словарь data передаем функцией render()
    return render(request, 'index.html')