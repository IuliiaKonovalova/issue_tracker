from django import forms
from .models import Project, Issue
from django.contrib.auth.models import User


# class ProjectForm(forms.ModelForm):
    
#     def __init__(self, personal=False, *args, **kwargs):
#         if personal:
#             super(ProjectForm, self).__init__(*args, **kwargs)
#             # hide collaborators field
#             self.fields['collaborators'].widget = forms.HiddenInput()
#         else:
#             super(ProjectForm, self).__init__(*args, **kwargs)
    
#     class Meta:
#         model = Project
#         fields = ['title', 'description', 'project_type', 'status', 'collaborators']
#         widgets = {
#                 'title': forms.TextInput(attrs={'class': 'form-control'}),
#                 'description': forms.Textarea(attrs={'class': 'form-control'}),
#                 'project_type': forms.Select(attrs={'class': 'form-control'}),
#                 'collaborators': forms.SelectMultiple(attrs={'class': 'form-control'}),
#             }


class PersonalProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
class TeamProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'collaborators']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'collaborators': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
                    
class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'description', 'priority', 'issue_type', 'assigned_to']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'issue_type': forms.Select(attrs={'class': 'form-control'}),
            'assigned_to': forms.Select(attrs={'class': 'form-control'}),
        }