from django.urls import path
from .views import ProjectsView, CreateProjectView, ProjectDetailView

urlpatterns = [
    path('', ProjectsView.as_view(), name='projects_list'),
    path('new/', CreateProjectView.as_view(), name='create_project'),
    path('<slug:created_by>/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
]