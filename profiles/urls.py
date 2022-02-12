from django.urls import path
from .views import UserProfileView


urlpatterns = [
    path('<username>/', UserProfileView.as_view(), name='user_profile'),
]
