from django.shortcuts import render, get_object_or_404, reverse
from django.views import  View
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


class UserProfileView(View):
    def get(self, request, *args, **kwargs):
        user_profile = get_object_or_404(User, username=kwargs['username'])
        return render(request, 'profiles/user_profile.html', {'user_profile': user_profile})