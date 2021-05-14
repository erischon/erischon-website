from django.shortcuts import render
from .models import Project
from website.forms import ContactForm


def portfolio_homepage(request):
    projects = Project.objects.all()
    contact_form = ContactForm(request.POST) 
    return render(request, 'portfolio/index.html', {'projects': projects, 'form': contact_form})


def project(request, id):
    project = Project.objects.get(id=id)
    return render(request, 'portfolio/project.html', {'project': project})
