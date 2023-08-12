from django.http import HttpResponse


def index(request):
    return HttpResponse("Contact Page.")

def sunny(request):
    return HttpResponse("sunny contact number.")
