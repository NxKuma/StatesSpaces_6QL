from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    ctx = {
        "tasks": [
        "task 1",
        "task 2",
        "task 3",
        "task 4"
        ]
    }
    return render(request, 'homepage.html',ctx)

def index(request):
    return HttpResponse('HelloWOrld')