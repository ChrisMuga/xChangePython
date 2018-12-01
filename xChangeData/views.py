from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    #return HttpResponse("Index")
    return render(request, 'home.html')
def user(request):
    return HttpResponse('User')