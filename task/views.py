from datetime import datetime

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from task.models import Task, Tag
from task.forms import TaskForm, TagForm


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task:task-list")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("task:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("task:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("task:tag-list")


def task_status_update(request, pk):
    task = Task.objects.get(id=pk)
    if task.is_done:
        task.is_done = False
        task.save()
    else:
        task.is_done = True
        task.save()
    return redirect("task:task-list")
