from django.shortcuts import render
from django.http import HttpResponse

from filesystem import walk


def home(request):
    startdir = request.GET.get('startdir')
    context = None
    if startdir:
        context = {'tree': walk(startdir), 'startdir':startdir}
    return render(request, 'filesystem/home.html', context)
