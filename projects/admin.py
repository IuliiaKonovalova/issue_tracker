from django.contrib import admin
from .models import Issue, Comment, Project
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    summernote_fields = ('description',)
    list_display = ('title', 'project_type', 'created_by', 'created_on', 'updated_on', 'status', )
    list_filter = ('created_on',)
    search_fields = ('name', 'created_by')
    ordering = ('-created_on',)
    list_select_related = ('created_by',)
    # need to add members to the project
    
    

@admin.register(Issue)
class IssueAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    list_display = ('title', 'created_by', 'created_on', 'status', 'priority', 'issue_type', 'votes_number')
    list_filter = ('created_on', 'status', 'priority', 'issue_type')
    search_fields = ('title', 'description')
    ordering = ('-created_on', 'status', 'priority')
    readonly_fields = ('created_on', 'updated_on',)
    list_select_related = ('created_by',)
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    summernote_fields = ('comment_body',)
    list_display = ('issue', 'created_by', 'created_on', 'updated_on')
    list_filter = ('created_on',)
    search_fields = ('issue', 'created_by')
    ordering = ('-created_on',)
    list_select_related = ('created_by',)
