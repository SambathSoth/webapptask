from django.shortcuts import render
from .models import Image

# Create your views here.
def home(request):
    images = Image.objects.all()
    context = {
        'images': images,
    }
    return render(request, 'index.html', context=context)

def detail1(request):
    return render(request, 'detail1.html')

def detail2(request):
    return render(request, 'detail2.html')