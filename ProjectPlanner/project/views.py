from django.shortcuts import render
from .models import Project
# Create your views here.
from .models import Task


def get_project(request, id):

    if request.method == "GET":
        project = Project.objects.get(id=id)
        return render(request,
                      'project/project-detail-view.html',
                      {'project': project, 'TaskPriority': Task.Priority})


# def get_project_tasks(request, id):

#     if request.method == "POST":
#         project = Project.objects.get(id=id)
#         tasks = project.tasks.all()
#         return render(request, )
