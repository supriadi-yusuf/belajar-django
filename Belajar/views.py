from django.http import HttpResponse
from django.shortcuts import render

#lokasi_template = "Belajar/Belajar/templates/html"
lokasi_template = "html"

def home(request):
    return HttpResponse('This is home')

def hello_world(request):
    return HttpResponse('Hello world!')

def indek1(request):
    return render( request, lokasi_template + '/belajar.index.html', {})

def base_demo(request):
    import os
    cwd = os.getcwd()
    html_template = cwd + '/templates/html/kerangka.html'
    return render( request, lokasi_template + '/base_demo.html', {
       'kerangka': html_template
    })
