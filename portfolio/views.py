from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Create your views here.
def portfolio(request):
    proyectos=Project.objects.all()
    return render(request,'portfolio/portfolio.html',{'projects':proyectos})