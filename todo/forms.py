from django import forms
from .models import ToDo

class TodoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = "__all__"