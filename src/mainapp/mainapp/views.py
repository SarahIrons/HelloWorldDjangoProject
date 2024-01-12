from django.shortcuts import render
from Profile.models import Profile

def home(request):
    context = {}
    print()
    return render(request, "home.html", context)

