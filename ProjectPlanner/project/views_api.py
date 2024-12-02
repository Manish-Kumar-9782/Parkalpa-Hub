from django.http import JsonResponse
import json
from project.models import Task
from project.forms import TaskRequiredForm


def updateTask(request):

    if request.method == "PATCH":
        data = json.loads(request.body)

        if not data:
            return JsonResponse({"status": "error", "message": "No data provided"}, status=400)

        task = Task.objects.get(pk=data.get("taskId"))

        task.isCompleted = data.get("isCompleted")
        task.save()
        return JsonResponse({"status": "success", "message": "Task updated successfully"}, status=200)

    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)


def addTask(request):

    if request.method == "POST":

        data = json.loads(request.body)
        print(data)
        if not data:
            return JsonResponse({"status": "error", "message": "No data provided"}, status=400)

        taskForm = TaskRequiredForm(data)

        if taskForm.is_valid():
            # taskForm.save()
            return JsonResponse({"status": "success", "message": "Task added successfully"}, status=201)

        else:
            print("Errors: ", taskForm.errors.as_data())
            return JsonResponse({"status": "error", "message": "Invalid data input", "details": taskForm.errors.as_json()}, status=400)

    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)
