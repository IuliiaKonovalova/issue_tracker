from django.shortcuts import render, get_object_or_404, reverse
from django.views import  View
from django.http import HttpResponseRedirect
from .models import UserProfile


class UserProfileView(View):
    def get(self, request, *args, **kwargs):
        user_profile = get_object_or_404(UserProfile, user=request.user)
        return render(request, 'profiles/user_profile.html', {'user_profile': user_profile})