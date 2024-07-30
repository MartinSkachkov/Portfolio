from django.shortcuts import render
from .models import Project

# Create your views here.
def index(request):
    return render(request, 'portfolio_app/index.html')

def display_projects(request):
    projects = Project.objects.all() # save all entries of the database to a variable
    print(projects[0].name)
    context = {'projects':projects}
    return render(request, 'portfolio_app/display_projects.html', context)

def contact(request):
    return render(request, 'portfolio_app/contact_me.html')