from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Hello world from homepage.")

def about(request):
    return HttpResponse("hello from aboutpage")