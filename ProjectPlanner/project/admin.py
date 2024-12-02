from django.contrib import admin
from .models import Task, Project, ProjectCategory
# Register your models here.

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(ProjectCategory)
