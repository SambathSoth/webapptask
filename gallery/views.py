from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def detail1(request):
    return render(request, 'detail1.html')

def detail2(request):
    return render(request, 'detail2.html')