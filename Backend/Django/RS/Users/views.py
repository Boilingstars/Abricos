from django.shortcuts import render, redirect
from .forms import UserLoginForm
from django.contrib.auth import login, authenticate

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = UserLoginForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password) # Проверяем учетные данные
            if user is not None:
                login(request, user)     # Выполняем вход
                return redirect('home')  # Перенаправляем на главную страницу
    return render(request, 'form.html', {'form': form})