from django.shortcuts import render
import subprocess
from django.http import JsonResponse

def run_script(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')  # Получаем данные из запроса
        # Запускаем скрипт и передаем данные
        result = subprocess.run(['python', 'Libs/ozon.py', data], capture_output=True, text=True)
        return JsonResponse({'output': result.stdout})  # Возвращаем результат
