from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'portfolio_app/index.html')

def display_projects(request):
    return render(request, 'portfolio_app/display_projects.html')