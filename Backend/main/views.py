from django.shortcuts import render, get_object_or_404

from main.models import Project


# Create your views here.

def home(request):
    return render(request, 'index.html')

def about_me(request):
    return render(request, 'About Me.html')

def cv(request):
    return render(request, 'cv.html')

def contact(request):
    return render(request, 'hire-me.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def Sample(request, id):
    project = get_object_or_404(Project, pk=id)
    return render(request, 'Sample.html', {'project': project})

