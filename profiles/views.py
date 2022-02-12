from django.shortcuts import render, get_object_or_404, reverse
from django.views import  View
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash



class UserProfileView(View):
    def get(self, request, *args, **kwargs):
        user_profile = get_object_or_404(User, username=kwargs['username'])
        if request.user.is_authenticated:
            # if user opens his own profile he can change his password
            if request.user == user_profile:
                # if user is authenticated and is opening his own profile
                # he can change his password
                form = PasswordChangeForm(request.user)
                return render(request, 'profiles/user_profile.html', {'user_profile': user_profile, 'password_form': form})
        return render(request, 'profiles/user_profile.html', {'user_profile': user_profile})
    
    # post method for changing password
    def post(self, request, *args, **kwargs):
        user_profile = get_object_or_404(User, username=kwargs['username'])
        if request.user.is_authenticated:
            # if user opens his own profile he can change his password
            if request.user == user_profile:
                # if user is authenticated and is opening his own profile
                # he can change his password
                form = PasswordChangeForm(request.user, request.POST)
                if form.is_valid():
                    user = form.save()
                    # update the session to reflect the changes
                    update_session_auth_hash(request, user)
                    return HttpResponseRedirect(reverse('user_profile', kwargs={'username': user_profile.username}))
                else:
                    return render(request, 'profiles/user_profile.html', {'user_profile': user_profile, 'password_form': form})
        return render(request, 'profiles/user_profile.html', {'user_profile': user_profile})