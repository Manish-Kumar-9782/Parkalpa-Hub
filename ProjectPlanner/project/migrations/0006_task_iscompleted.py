# Generated by Django 5.1.1 on 2024-12-01 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_rename_sub_task_task_parenttask'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='isCompleted',
            field=models.BooleanField(default=False),
        ),
    ]