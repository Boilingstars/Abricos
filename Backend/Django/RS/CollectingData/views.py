from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests

# Функция приема запроса от Vue и отправки запроса AIserver

@csrf_exempt  # Отключаем CSRF для упрощения (в продакшене используйте более безопасные методы)
def CollectingDataList(request):
    if request.method == 'POST':
        body = json.loads(request.body)  # Извлекаем данные из тела запроса
        # Отправляем данные на сервер AI
        ai_response = requests.post('http://http://192.168.20.83:8001//run-script/', json=body)
        return JsonResponse(ai_response.json())  # Возвращаем ответ от сервера AI
