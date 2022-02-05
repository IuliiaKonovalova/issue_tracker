from re import L
from django.contrib import admin
from .models import Issue, Comment, Project, UserProfile
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Issue)
class IssueAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    list_display = ('title', 'created_by', 'created_on', 'status', 'priority', 'type', 'votes_number')
    list_filter = ('created_on', 'status', 'priority', 'type')
    search_fields = ('title', 'description')
    ordering = ('-created_on', 'status', 'priority', 'type')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_on', 'updated_on',)
    list_select_related = ('created_by',)
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('issue', 'created_by', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('issue', 'created_by')
    ordering = ('-created_on',)
    list_select_related = ('created_by',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('name', 'created_by')
    ordering = ('-created_on',)
    list_select_related = ('created_by',)
    # need to add members to the project
    
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'birth_date')
    # display assigned issues
    
    # display projects
    
    