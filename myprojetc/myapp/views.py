from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = 'We Have The Best Services'
    return render(request, 'index.html', 'feature': feature1)

def counter(request):
    text = request.POST['text']
    number_of_words = len(text.split())
    return render(request, 'counter.html', {'number': number_of_words})

# Practice