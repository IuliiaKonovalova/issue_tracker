from django import forms
from .models import Project, Issue, Comment
from django.contrib.auth.models import User


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
            'collaborators': forms.SelectMultiple(
                attrs={'class': 'form-control'}
                ),
        }


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = [
            'title',
            'description',
            'priority',
            'issue_type',
            'assigned_to'
            ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            # 'priority': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.RadioSelect(attrs={'class': 'form-control'}),
            # 'issue_type': forms.Select(attrs={'class': 'form-control'}),
            'issue_type': forms.RadioSelect(attrs={'class': 'form-control'}),
            'assigned_to': forms.Select(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_body']
        widgets = {
            'comment_body': forms.Textarea(attrs={'class': 'form-control'}),
        }
