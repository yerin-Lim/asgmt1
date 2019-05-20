from django.shortcuts import render

# Create your views here.
def basic(request):
    return render(request, 'basic.html')

def about(request):
    return render(request, 'about.html')