from django.shortcuts import render

def index(request):
    data = {} # Словарь data передаем функцией render()
    return render(request, 'index.html')
