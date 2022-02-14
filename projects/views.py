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
        issues_to_do = issues.filter(status=0)
        issues_in_progress = issues.filter(status=1)
        issues_done = issues.filter(status=2)
        context = {
            'project': project,
            'issues_to_do': issues_to_do,
            'issues_in_progress': issues_in_progress,
            'issues_done': issues_done,
        }
        return render(request, 'projects/project_detail.html', context)
    

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
            return HttpResponseRedirect(reverse('project_detail', kwargs={'created_by': project.created_by,'pk': project.id}))
        return render(request, 'projects/create_issue.html', {'form': form, 'project':project})


class IssueDetailView(View):
    def get(self, request, issue_id, *args, **kwargs):
        issue = get_object_or_404(Issue, id=issue_id)
        comments = Comment.objects.filter(issue=issue)
        context = {
            'issue': issue,
            'comments': comments,
        }
        return render(request, 'projects/issue_detail.html', context)

class IssueVotesView(View):
    def post(self, request, issue_id, *args, **kwargs):
        issue = get_object_or_404(Issue, id=issue_id)
        project = get_object_or_404(Project, id=issue.project.id)
        if issue.votes.filter(id=request.user.id).exists():
            issue.votes.remove(request.user)
        else:
            issue.votes.add(request.user)
        return HttpResponseRedirect(reverse('issue_detail', args=[project.created_by, project.id, issue.id]))
    
    
class EditProjectView(View):
    def get(self, request, project_id, *args, **kwargs):
        project = get_object_or_404(Project, id=project_id)
        if project.project_type == 0:
            form = PersonalProjectForm(instance=project)
        else:
            form = TeamProjectForm(instance=project)
            
        return render(request, 'projects/edit_project.html', {'form': form, 'project': project})
    
    def post(self, request, project_id, *args, **kwargs):
        project = get_object_or_404(Project, id=project_id)
        if project.project_type == 0:
            form = PersonalProjectForm(request.POST, instance=project)
        else:
            form = TeamProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('project_detail', kwargs={'created_by': project.created_by,'pk': project.id}))
        return render(request, 'projects/edit_project.html', {'form': form, 'project': project})
    
class EditIssueView(View):
    def get(self, request, issue_id, *args, **kwargs):
        issue = get_object_or_404(Issue, id=issue_id)
        form = IssueForm(instance=issue)
        return render(request, 'projects/edit_issue.html', {'form': form, 'issue': issue})
    
    def post(self, request, issue_id, *args, **kwargs):
        issue = get_object_or_404(Issue, id=issue_id)
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('issue_detail', args=[issue.created_by, issue.project.id, issue.id]))
        return render(request, 'projects/edit_issue.html', {'form': form, 'issue': issue})