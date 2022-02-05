from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Issue, Comment, Project
# Create your views here.


class ProjectsListView(generic.ListView):
    model = Project
    queryset = Project.objects.filter
    template_name = 'projects/projects_list.html'
    context_object_name = 'projects'
    
