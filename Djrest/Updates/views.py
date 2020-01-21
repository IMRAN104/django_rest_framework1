from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def json_example_view(request):
    data = {
        'name': 'Imran',
        'age': 24,
        'occupation': 'service holder!',
        'expertise': 'can pass enormous amount of time on home entertainment!'
    }
    return JsonResponse(data)
