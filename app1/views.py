from django.shortcuts import render

# Create your views here.

def home(request):
    context=dict()
    return render(request, "index.html",context=context)

def image(request):
    context=dict()
    return render(request, "home.html",context=context)
