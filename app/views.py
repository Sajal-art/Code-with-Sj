from django.shortcuts import render
from django.http.response import HttpResponse
from app.models import Service , State , City
# Create your views here.

def home(request):
    Services=Service.objects.all()
    cities=City.objects.all()
    states=State.objects.all()

    context={
        'services': Services,
        'cities': cities,
        'states': states
    }
    return render(request, template_name='app/index.html', context=context)