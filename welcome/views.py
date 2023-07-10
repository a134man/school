from django.shortcuts import render
from django.http import HttpResponse

# Home page
def index(request):
    context = {}
    return render(request, "welcome/index.html", context)
