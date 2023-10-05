from django import forms


from task.models import Task, Tag


class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime"


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={"class": "form-control"}
        )
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
        widgets = {
            "content": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": " Enter task content"}
            ),
            "deadline": forms.DateTimeInput(
                attrs={"type": "datetime-local",
                       "class": "form-control"}
            )
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
