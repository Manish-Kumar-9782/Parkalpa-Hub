# Generated by Django 5.1.1 on 2024-12-01 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_remove_project_tasks_task_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='sub_task',
            new_name='parentTask',
        ),
    ]