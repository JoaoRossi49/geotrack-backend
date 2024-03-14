from django.shortcuts import render

def Mapa(request):
    markers = [
        {'lat': 51.5074, 'lng': -0.1278, 'popupText': 'London'},
        {'lat': 40.7128, 'lng': -74.0060, 'popupText': 'New York'},
    ]
    context = {
        'markers': markers
    }
    return render(request, 'mapa.html', context)
