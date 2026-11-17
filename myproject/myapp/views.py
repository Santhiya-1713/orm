from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Welcome to the home page")
def about(request):
    return HttpResponse("This is the About page")
def contact(request):
    return HttpResponse("Contact us at info@csccomputereducation.edu.in.")