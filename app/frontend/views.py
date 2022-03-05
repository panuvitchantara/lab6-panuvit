from django.shortcuts import render

# Create your views here.
def displayCount(request):
    return render(request, 'frontend/index.html')