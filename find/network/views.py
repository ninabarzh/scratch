from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, world. You're at the network home.")

def browser(request):
    return HttpResponse("Hello, world. You're at the network browser home.")
