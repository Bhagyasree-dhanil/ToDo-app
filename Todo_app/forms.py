from django import forms
from .models import todo_db

class todo_form(forms.ModelForm):
    class Meta:
        model = todo_db
        fields = ['title','memo','important']
