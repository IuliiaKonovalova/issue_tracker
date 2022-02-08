from django.urls import path
from .views import ProjectsView, CreateProjectView

urlpatterns = [
    path('', ProjectsView.as_view(), name='projects_list'),
    path('new/', CreateProjectView.as_view(), name='create_project'),
]