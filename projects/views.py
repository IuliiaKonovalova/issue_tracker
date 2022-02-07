from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Issue, Comment, Project
# Create your views here.


# view to show all projects created by the user and projects he is a collaborator of
class ProjectsView(generic.ListView):
    model = Project
    template_name = 'projects/projects_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.filter(
            collaborators=self.request.user
        )