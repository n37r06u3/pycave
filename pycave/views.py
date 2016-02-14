from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html', locals())


def project(request):
    return render(request, 'project.html', locals())

def service(request):
    return render(request, 'service.html', locals())

def about(request):
    return render(request, 'about.html', locals())

def contact(request):
    return render(request, 'contact.html', locals())

