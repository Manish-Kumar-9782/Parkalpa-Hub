# Generated by Django 5.1.1 on 2024-09-17 18:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_project_profile_image_alter_project_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='tasks',
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tasks', to='project.project'),
        ),
    ]
