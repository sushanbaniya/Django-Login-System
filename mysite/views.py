from django.shortcuts import render
from django.http import HttpResponse
from mysite.models import Students

# Create your views here.

def index(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        email = request.POST.get('email')

        s = Students(firstname=firstname, email=email)
        s.save()

    return render(request, 'mysite/index.html')