from django.contrib import admin
from .models import UserProfile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'username', 'email')
    list_filter = ('user', 'username', 'email')
    search_fields = ('user', 'username', 'email')
    ordering = ('user', 'username', 'email')
    list_select_related = ('user',)
