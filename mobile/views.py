from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def samsung(request):
    return render(request,'samsung.html')

def oppo(request):
    return HttpResponse('Its OPPO mobile')