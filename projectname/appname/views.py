from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User

# Create your views here.
def mainpage(request):
    template = get_template('mainpage.html')
    variables = Context({
        'appname': 'electrosobres',
        'titilepage': 'sobres',
        'author': 'Luis Barcenas'
    })
    page = template.render(variables)
    return HttpResponse(page)


def dashboard(request, uname):
    try:
        user = User.objects.get(username=uname)
    except:
        raise Http404('El usuario no existe')

    sobres = user.sobre_set.all()
    template = get_template('dashboard.html')
    variables = Context({
        'username': uname,
        'author': 'Luis Barcenas',
        'sobres': sobres
    })
    page = template.render(variables)
    return HttpResponse(page)
