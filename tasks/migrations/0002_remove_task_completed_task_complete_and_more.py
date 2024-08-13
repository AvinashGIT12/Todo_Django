# Generated by Django 4.2.13 on 2024-06-27 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="task", name="completed",),
        migrations.AddField(
            model_name="task",
            name="complete",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="task",
            name="created",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
