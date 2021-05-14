from django.shortcuts import render
from .models import Project


def portfolio_homepage(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/index.html', {'projects': projects})


def project(request, id):
    project = Project.objects.get(id=id)
    return render(request, 'portfolio/project.html', {'project': project})
