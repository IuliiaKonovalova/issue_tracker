from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect, JsonResponse
from .models import Issue, Comment, Project
from .forms import PersonalProjectForm, TeamProjectForm, IssueForm, CommentForm
from django.contrib.auth.models import User



class ProjectsView(View):
    def get(self, request):
        users_projects = Project.objects.filter(created_by=request.user)
        # projects not created by user but where user in in collaborators
        collab_projects = request.user.collaborated_projects.all().exclude(created_by=request.user)
        return render(request, 'projects/projects_list.html', {'users_projects': users_projects, 'collab_projects': collab_projects})
        
        
class CreatePersonalProjectView(View):
    def get(self, request):
        form = PersonalProjectForm()
        return render(request, 'projects/create_project.html', {'form': form, 'personal': True})
    def post(self, request):
        form = PersonalProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.status = 0
            project.project_type = 0
            project.save()
            project.collaborators.add(request.user)
            project.save()
            return HttpResponseRedirect(reverse('projects_list'))
        return render(request, 'projects/create_project.html', {'form': form})
        
class CreateTeamProjectView(View):
    def get(self, request):
        form = TeamProjectForm()
        # query list for collaborators should not include the current user
        form.fields['collaborators'].queryset = User.objects.exclude(id=request.user.id)
        return render(request, 'projects/create_project.html', {'form': form, 'personal': False})
    def post(self, request):
        form = TeamProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.project_type = 1
            project.created_by = request.user
            project.status = 0
            project.save()
            form.save_m2m()
            project.collaborators.add(request.user)
            project.save()
            return HttpResponseRedirect(reverse('projects_list'))
        return render(request, 'projects/create_project.html', {'form': form})
        

class ProjectDetailView(View):
    def get(self, request, created_by, pk, *args, **kwargs):
        # project = get_object_or_404(Project, pk=pk)
        project = get_object_or_404(Project, pk=pk, created_by__username=created_by)
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
    def get(self, request, created_by, project_id, *args, **kwargs):
        project = get_object_or_404(Project, id=project_id, created_by__username=created_by)
        form = IssueForm()
        return render(request, 'projects/create_issue.html', {'form': form, 'project': project})
    
    def post(self, request, created_by, project_id, *args, **kwargs):
        form = IssueForm(request.POST)
        project = get_object_or_404(Project, id=project_id, created_by__username=created_by)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.created_by = request.user
            issue.project = get_object_or_404(Project, id=project_id)
            issue.save()
            return HttpResponseRedirect(reverse('project_detail', kwargs={'created_by': project.created_by,'pk': project.id}))
        return render(request, 'projects/create_issue.html', {'form': form, 'project':project})


class IssueDetailView(View):
    def get(self, request, created_by, project_id, issue_id, *args, **kwargs):
        # issue = get_object_or_404(Issue, id=issue_id)
        project = get_object_or_404(Project, id=project_id, created_by__username=created_by)
        issue = project.issues.get(id=issue_id)
        comments = Comment.objects.filter(issue=issue)
        form = CommentForm()
        context = {
            'issue': issue,
            'comments': comments,
            'form': form,
        }
        return render(request, 'projects/issue_detail.html', context)

    def post(self, request, created_by, project_id, issue_id, *args, **kwargs):
        form = CommentForm(request.POST)
        # issue = get_object_or_404(Issue, id=issue_id)
        project = get_object_or_404(Project, id=project_id, created_by__username=created_by)
        issue = project.issues.get(id=issue_id)
        # project = get_object_or_404(Project, id=issue.project.id)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.created_by = request.user
            comment.issue = issue
            comment.save()
            return HttpResponseRedirect(reverse('issue_detail', args=[project.created_by, project.id, issue.id]))
        return render(request, 'projects/issue_detail.html', {'form': form, 'issue': issue})


class IssueVotesView(View):
    def post(self, request, created_by, project_id, issue_id, *args, **kwargs):
        project = get_object_or_404(Project, id=project_id, created_by__username=created_by)
        issue = project.issues.get(id=issue_id)
        if issue.votes.filter(id=request.user.id).exists():
            issue.votes.remove(request.user)
        else:
            issue.votes.add(request.user)
        return HttpResponseRedirect(reverse('issue_detail', args=[project.created_by, project.id, issue.id]))


class EditProjectView(View):
    def get(self, request, created_by, project_id, *args, **kwargs):
        project = get_object_or_404(Project, id=project_id, created_by__username=created_by)
        if project.project_type == 0:
            form = PersonalProjectForm(instance=project)
        else:
            form = TeamProjectForm(instance=project)
            
        return render(request, 'projects/edit_project.html', {'form': form, 'project': project})
    
    def post(self, request, created_by, project_id, *args, **kwargs):
        project = get_object_or_404(Project, id=project_id, created_by__username=created_by)
        if project.project_type == 0:
            form = PersonalProjectForm(request.POST, instance=project)
        else:
            form = TeamProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('project_detail', kwargs={'created_by': project.created_by,'pk': project.id}))
        return render(request, 'projects/edit_project.html', {'form': form, 'project': project})


class EditIssueView(View):
    def get(self, request, created_by, project_id, issue_id, *args, **kwargs):
        # issue = get_object_or_404(Issue, id=issue_id)
        project = get_object_or_404(Project, id=project_id, created_by__username=created_by)
        issue = project.issues.get(id=issue_id)
        form = IssueForm(instance=issue)
        return render(request, 'projects/edit_issue.html', {'form': form, 'issue': issue})
    
    def post(self, request, created_by, project_id, issue_id, *args, **kwargs):
        # issue = get_object_or_404(Issue, id=issue_id)
        project = get_object_or_404(Project, id=project_id, created_by__username=created_by)
        issue = project.issues.get(id=issue_id)
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('issue_detail', args=[issue.created_by, issue.project.id, issue.id]))
        return render(request, 'projects/edit_issue.html', {'form': form, 'issue': issue})


class UpdateIssueStatusAjaxView(View):
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            issue_id = request.POST.get('issue_id')
            status = request.POST.get('issue_status')
            issue = get_object_or_404(Issue, id=issue_id)
            issue.status = status
            issue.save()
            return JsonResponse({'status': 'ok'})
        
        
class UpdateCommentAjaxView(View):
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            comment_id = request.POST.get('comment_id')
            comment_text = request.POST.get('comment_body')
            comment = get_object_or_404(Comment, id=comment_id)
            comment.comment_body = comment_text
            comment.save()
            return JsonResponse({'status': 'ok'})
        
        
class DeleteIssueView(View):
    def get(self, request, created_by, project_id, issue_id, *args, **kwargs):
        project = get_object_or_404(Project, id=project_id, created_by__username=created_by)
        issue = project.issues.get(id=issue_id)
        if issue.created_by == request.user or project.created_by == request.user:
            issue.delete()
            return HttpResponseRedirect(reverse('project_detail', kwargs={'created_by': project.created_by,'pk': project.id}))
        return HttpResponseRedirect(reverse('issue_detail', args=[project.created_by, issue.project.id, issue.id]))
    

class DeleteProjectView(View):
    def get(self, request, project_id, *args, **kwargs):
        project = get_object_or_404(Project, id=project_id)
        if request.user == project.created_by:
            return render(request, 'projects/delete_project.html', {'project': project})
        else:
            return HttpResponseRedirect(reverse('project_detail', kwargs={'created_by': project.created_by,'pk': project.id}))
    
    def post(self, request, project_id, *args, **kwargs):
        project = get_object_or_404(Project, id=project_id)
        project.delete()
        return HttpResponseRedirect(reverse('projects_list'))
    

class DeleteCommentAjaxView(View):
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            comment_id = request.POST.get('comment_id')
            comment = get_object_or_404(Comment, id=comment_id)
            comment.delete()
            return JsonResponse({'status': 'ok'})
