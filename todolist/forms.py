from django import forms
from .models import ToDo


class ToDoForm(forms.ModelForm):

    class Meta:
        model = ToDo
        fields = 'name', 'status_id', 'priority', 'details'

        # adds class attributes to html elements rendered by django model forms
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'status_id' : forms.Select(attrs={'class': 'form-control'}),
            'priority' : forms.Select(attrs={'class': 'form-control'}),
            'details' : forms.TextInput(attrs={'class': 'form-control'}),
        }