from django import forms
from matplotlib import widgets
from .models import Project, Issue


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        # need to allow user to create title and description
        # need to allow user to chose type of project (personal or team)
        # if team project, need to allow user to invite team members
        
        fields = ['title', 'description', 'project_type', 'collaborators']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'project_type': forms.Select(attrs={'class': 'form-control'}),
            'collaborators': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
        
        def __init__(self, *args, **kwargs):
            super(ProjectForm, self).__init__(*args, **kwargs)
            if self.instance.id:
                if self.instance.project_type == 0:
                    self.fields['collaborators'].widget = forms.HiddenInput()
                else:
                    self.fields['collaborators'].widget = forms.SelectMultiple(attrs={'class': 'form-control'})
                    
class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'description', 'priority', 'issue_type', 'status', 'assigned_to']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'issue_type': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'assigned_to': forms.Select(attrs={'class': 'form-control'}),
        }