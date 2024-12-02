from django.shortcuts import render, redirect
from project.models import Project


def home(request):

    if request.user.is_authenticated:

        projects = Project.objects.all()

        return render(request, "home.html",  {"projects": projects})

    return redirect("login")
