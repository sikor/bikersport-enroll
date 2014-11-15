from django.shortcuts import render

# Create your views here.


def event(request, name):
    return render(request, 'enrollapp/event.html')