from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def noticias(request):
    return render(request, 'main/index.html')

def artigos(request):
    return render(request, 'main/index.html')

def contribs(request):
    return render(request, 'main/index.html')

def sobre(request):
    return render(request, 'main/index.html')
