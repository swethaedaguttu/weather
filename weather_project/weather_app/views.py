# weather_app/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .weather import get_weather

def index(request):
    return render(request, 'index.html')

def get_weather_view(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        if city:
            weather = get_weather(city)
            return JsonResponse(weather)
        else:
            return JsonResponse({'error': 'City parameter missing'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
