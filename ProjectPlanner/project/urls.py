from django.urls import path
from .views import get_project
from .views_api import updateTask, addTask

api_urls = [
    path("api/tasks/update", view=updateTask, name="update_task"),
    path("api/tasks/add", view=addTask, name="add_task"),
]


urlpatterns = [
    path("view/<int:id>", view=get_project, name="view_project")
] + api_urls
