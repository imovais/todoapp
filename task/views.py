from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def page1(request):
    return HttpResponse("This is Page One.")