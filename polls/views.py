from django.http import HttpResponse


def index(request):
    return HttpResponse("at the index.")
