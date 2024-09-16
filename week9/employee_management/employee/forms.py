from django import forms
from .models import Employee, Project
from django.core.exceptions import ValidationError
from datetime import date

class EmployeeForm(forms.ModelForm):
    Gender_choice = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('LGBT', 'LGBT'),
    )

    gender = forms.ChoiceField(choices=Gender_choice)  # Override choice field

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'gender', 'birth_date', 'hire_date', 'salary', 'position']
        widgets = {
            'birth_date': forms.TextInput(attrs={'type': 'date'}),
            'hire_date': forms.TextInput(attrs={'type': 'date'}),
        }

    def clean_hire_date(self):
        hire_date = self.cleaned_data.get('hire_date')
        if hire_date > date.today():
            raise ValidationError("Hire date cannot be in the future.")
        return hire_date

class Projectform(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'manager', 'due_date','start_date', 'description']
        widgets = {
            'start_date': forms.TextInput(attrs={'type': 'date'}),
            'due_date': forms.TextInput(attrs={'type': 'date'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        due_date = cleaned_data.get('due_date')

        if start_date and due_date and start_date > due_date:
            raise ValidationError("Start date must be before the due date.")
        return cleaned_data 

class DetailForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name','start_date', 'due_date', 'description','manager', 'staff']
        widgets = {
            'start_date': forms.TextInput(attrs={'type': 'date'}),
            'due_date': forms.TextInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        due_date = cleaned_data.get('due_date')

        if start_date and due_date and start_date > due_date:
            raise ValidationError("Start date must be before the due date.")
        return cleaned_data 