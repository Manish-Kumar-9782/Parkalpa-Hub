# Generated by Django 5.1.1 on 2024-09-17 14:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tasks',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tasks', to='project.task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='sub_task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_tasks', to='project.task'),
        ),
    ]
