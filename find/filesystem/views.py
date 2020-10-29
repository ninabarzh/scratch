from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader

from .models import Filesystem

def home(request):
    return HttpResponse("Hello, world. You're at the filesystem home.")


def browser(request):
    fslist = Filesystem.objects.order_by('name')[:10]
    template = loader.get_template('filesystem/browser.html')
    context = {
        'fslist': fslist,
    }
    return HttpResponse(template.render(context, request))


def directory(request, name, path):
    try:
        fs = Filesystem.objects.get(name)
    except ValueError:
        raise Http404
    except Filesystem.DoesNotExist:
        raise Http404
    except IOError:
        raise Http404
    if fs.isdir(path):
        files = fs.files(path)
        context = {
            'dlist': [f for (f, d, t) in files if d],
            'flist': [{'name': f, 'type': t} for (f, d, t) in files if not d],
            'path': path,
            'fs': fs,
        }
        return render(request, 'filesystem/directory.html', context)
    else:
        (f, mimetype) = fs.file(path)
    return HttpResponse(open(f).read(), mimetype=mimetype)


def analysis():
    return None
