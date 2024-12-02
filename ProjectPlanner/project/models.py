from django.db import models
from datetime import date
# Create your models here.


class ProjectCategory(models.Model):
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Task(models.Model):

    class Priority(models.TextChoices):
        LOW = 'low', 'Low'
        MEDIUM = 'medium', 'Medium'
        HIGH = 'high', 'High'
        URGENT = 'urgent', 'Urgent'

    class Status(models.TextChoices):
        IN_PROGRESS = ('in_progress', 'In Progress')
        COMPLETED = ('completed', 'Completed')
        PENDING = ('pending', 'Pending')
        INACTIVE = ("inactive", "Inactive")

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    due_date = models.DateField()
    priority = models.CharField(
        max_length=8,  choices=Priority.choices, default=Priority.LOW)
    status = models.CharField(
        max_length=15, choices=Status.choices, default=Status.PENDING)

    project = models.ForeignKey(
        "Project",  on_delete=models.DO_NOTHING, related_name="tasks", null=True, blank=True)

    parentTask = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name="sub_tasks", null=True, blank=True)
    # if a task has a parent then it must be mentioned by sub task
    is_sub_task = models.BooleanField(default=False)
    # if a task has  sub tasks then it must be mentioned by parent and has tasks
    has_sub_tasks = models.BooleanField(default=False)

    isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Project(models.Model):

    class Status(models.TextChoices):
        IN_PROGRESS = 'in_progress', 'In Progress'
        COMPLETED = 'completed', 'Completed'
        PENDING = 'pending', 'Pending'
        INITIATED = 'initiated', 'Initiated'
        UPCOMING = 'upcoming', 'Upcoming'
        INACTIVE = 'inactive', 'Inactive'

    profile_image = models.ImageField(
        upload_to="media/images/", null=True, blank=True)

    project_name = models.CharField(max_length=50)
    project_title = models.CharField(max_length=100)
    # the date on which project is added.
    added_date = models.DateField(auto_now_add=True)
    # the date on which  project is start or will start.
    start_date = models.DateField()
    end_date = models.DateField()  # the date on which project should be ended.
    description = models.TextField(max_length=500)
    category = models.ForeignKey(ProjectCategory,  on_delete=models.DO_NOTHING)
    status = models.CharField(
        max_length=15,  choices=Status.choices, default='inactive')

    def __str__(self):
        return self.project_name

    def isNew(self):
        if (self.added_date - date.today()).days <= 10:
            return True
        return False

    def total_tasks(self):
        return self.get_tasks().count()

    def get_tasks(self):
        return self.tasks.all()

    def completed_tasks(self):
        return self.tasks.filter(status=self.Status.COMPLETED)

    def total_completed_tasks(self):
        return self.completed_tasks().count()
