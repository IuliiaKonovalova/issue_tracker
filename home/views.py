from django.shortcuts import render
from django.http import HttpResponseRedirect


def index(request):
    """ Return index page """
    if request.user.is_authenticated:
        return HttpResponseRedirect('/projects/')
    return render(request, 'home/index.html')
