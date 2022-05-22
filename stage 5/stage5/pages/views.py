from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def page1(request):
    return HttpResponse("""<h1> KODECAMP Page 1</h1>""")

def page2(request):
    return HttpResponse("""<h1> KODECAMP Page 2</h1>""")

def page3(request):
    return HttpResponse("""<h1> KODECAMP Page 3</h1>""")    