from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from rest_framework import generics
from Main.models import Projects
from Main.serializer import ProjectsSerializer

class ProjectList(generics.ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

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
    if request.method == 'GET':
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