from django.urls import path
from .views import ProjectsView, CreatePersonalProjectView, CreateTeamProjectView, ProjectDetailView, CreateIssueView, IssueDetailView

urlpatterns = [
    path('', ProjectsView.as_view(), name='projects_list'),
    path('new_personal_project/', CreatePersonalProjectView.as_view(), name='create_personal_project'),
    path('new_team_project/', CreateTeamProjectView.as_view(), name='create_team_project'),
    path('<slug:created_by>/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('<slug:created_by>/<int:project_id>/new_issue/', CreateIssueView.as_view(), name='create_issue'),
    path('<slug:created_by>/<int:project_id>/<int:issue_id>/', IssueDetailView.as_view(), name='issue_detail'),
]