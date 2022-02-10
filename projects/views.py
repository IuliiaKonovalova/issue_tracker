from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Issue, Comment, Project
from .forms import ProjectForm
# Create your views here.


# view to show all projects created by the user and projects he is a collaborator of
# class ProjectsView(generic.ListView):
#     model = Project
#     template_name = 'projects/projects_list.html'
#     context_object_name = 'projects'

#     def get_queryset(self):
#         return Project.objects.filter(
#             collaborators=self.request.user
#         )
class ProjectsView(View):
    def get(self, request):
        # chaeck if current user is in collaborators of the project
        projects = Project.objects.all()
        return render(request, 'projects/projects_list.html', {'projects': projects})
        
        
        
class CreateProjectView(View):
    def get(self, request):
        form = ProjectForm()
        return render(request, 'projects/create_project.html', {'form': form})
    
    def post(self, request):
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()
            return HttpResponseRedirect(reverse('projects_list'))
        return render(request, 'projects/create_project.html', {'form': form})
    

class ProjectDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        project = get_object_or_404(Project, pk=pk)
        return render(request, 'projects/project_detail.html', {'project': project})