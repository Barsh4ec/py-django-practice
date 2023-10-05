from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=127)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    def __str__(self) -> str:
        return f"{self.content}, {self.deadline} (done={self.is_done})"
