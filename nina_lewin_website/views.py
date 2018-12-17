from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the Nina's.")
    
def title(request):
    return render(request, 'nina_lewin_website/index.html', {})
