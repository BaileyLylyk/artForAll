from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def construction_view(request, *args, **kwargs):
    return HttpResponse("<h1> This site is currently being constructed. Please check back later </h1>")

def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

