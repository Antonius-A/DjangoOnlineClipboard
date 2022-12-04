from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Clipboards
# from random_ui_generator import random_generate_alpha_numberic as rgan
import random, string


def random_generate_alpha_numberic(length: int = 16):
    ui_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    # print(ui_string)
    return ui_string


def index(request):
    allclipboards = Clipboards.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'allclipboards': allclipboards,
    }
    return HttpResponse(template.render(context, request))


def view(request, ui):
    thisclipboard = Clipboards.objects.get(ui=ui)
    template = loader.get_template('view.html')
    context = {
        'thisclipboard': thisclipboard,
    }
    return HttpResponse(template.render(context, request))

def search(request):
    ui = request.POST.get('ui','')
    print(ui)
    thisclipboard = Clipboards.objects.get(ui=ui)
    print(thisclipboard)
    template = loader.get_template('view.html')
    context = {
        'thisclipboard': thisclipboard,
    }
    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template('add.html')

    context = {
        'random_alpha_numeric': random_generate_alpha_numberic(20),
    }
    return HttpResponse(template.render(context, request))


def addclipboard(request):

    ui_hidden = request.POST['ui-hidden']
    print(ui_hidden)
    ui = request.POST.get('ui', ui_hidden);
    content = request.POST['content']
    passcode = request.POST['passcode']
    passcode_hint = request.POST['passcode_hint']
    if request.POST['minutes_until_expired'] == '':
        minutes_until_expired = 1440
    else:
        minutes_until_expired = int(request.POST['minutes_until_expired'])

    thisclipboard = Clipboards(ui=ui, content=content, passcode=passcode, passcode_hint=passcode_hint,
                               minutes_until_expired=minutes_until_expired)
    thisclipboard.save()
    return HttpResponseRedirect(reverse('index'))


def delete(request, ui):
    thisclipboard = Clipboards.objects.get(ui=ui)
    thisclipboard.delete()
    return HttpResponseRedirect(reverse('index'))


def update(request, ui):
    thisclipboard = Clipboards.objects.get(ui=ui)
    template = loader.get_template('update.html')
    context = {
        'thisclipboard': thisclipboard,
    }
    return HttpResponse(template.render(context, request))


def updateclipboard(request, ui):
    content = request.POST['content']
    passcode = request.POST['passcode']
    minutes_until_expired = int(request.POST["minutes_until_expired"])
    thisclipboard = Clipboards.objects.get(ui=ui)
    if thisclipboard.passcode == passcode:
        thisclipboard.content = content
        thisclipboard.minutes_until_expired = minutes_until_expired
        thisclipboard.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('passcode-error'))


def passcode_error(request):
    template = loader.get_template('passcode-error.html')
    context = {
        'message': "your passcode did not match, clipboard was not changed",
    }
    return HttpResponse(template.render(context, request))
