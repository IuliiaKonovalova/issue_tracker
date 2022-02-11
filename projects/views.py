from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Issue, Comment, Project
from .forms import PersonalProjectForm, TeamProjectForm, IssueForm



class ProjectsView(View):
    def get(self, request):
        # chaeck if current user is in collaborators of the project
        projects = Project.objects.all()
        return render(request, 'projects/projects_list.html', {'projects': projects})
        
        
class CreatePersonalProjectView(View):
    def get(self, request):
        form = PersonalProjectForm()
        return render(request, 'projects/create_project.html', {'form': form, 'personal': True})
    def post(self, request):
        form = PersonalProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()
            project.collaborators.add(request.user)
            project.status = 0
            project.project_type = 0
            project.slug = project.title.replace(' ', '-').lower()
            project.save()
            return HttpResponseRedirect(reverse('projects_list'))
        return render(request, 'projects/create_project.html', {'form': form})
        
class CreateTeamProjectView(View):
    def get(self, request):
        form = TeamProjectForm()
        return render(request, 'projects/create_project.html', {'form': form, 'personal': False})
    def post(self, request):
        form = TeamProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.project_type = 1
            project.created_by = request.user
            project.save()
            # project.collaborators.add(request.user)
            project.status = 0
            project.slug = project.title.replace(' ', '-').lower()
            project.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('projects_list'))
        return render(request, 'projects/create_project.html', {'form': form})
        

class ProjectDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        project = get_object_or_404(Project, pk=pk)
        issues = Issue.objects.filter(project=project)
        return render(request, 'projects/project_detail.html', {'project': project, 'issues': issues})
    

class CreateIssueView(View):
    def get(self, request, project_id, *args, **kwargs):
        project = get_object_or_404(Project, id=project_id)
        form = IssueForm()
        return render(request, 'projects/create_issue.html', {'form': form, 'project': project})
    
    def post(self, request, project_id, *args, **kwargs):
        form = IssueForm(request.POST)
        project = get_object_or_404(Project, id=project_id)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.created_by = request.user
            issue.project = get_object_or_404(Project, id=project_id)
            issue.save()
            return render(request, 'projects/project_detail.html', {'project': project})
        return render(request, 'projects/create_issue.html', {'form': form, 'project':project})
    