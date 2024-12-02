from django import forms
from .models import Task


class TaskRequiredForm(forms.ModelForm):
    """A Task Form model which include minimal required fields.

    included: title, description, priority, due_date
    """
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'due_date']
