from django.http import HttpResponse


def index(request):
    return HttpResponse('Fuck you, dude.')
