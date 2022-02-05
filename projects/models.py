from django.db import models
from django.contrib.auth.models import User

# models for issue tracker app

ISSUE_STATUS = (
    (0, 'Open'),
    (1, 'Closed'),
    (2, 'In Progress'),
)

ISSUE_PRIORITY = (
    (0, 'Low'),
    (1, 'Medium'),
    (2, 'High'),
    (3, 'Urgent'),
)

ISSUE_TYPE = (
    (0, 'Bug'),
    (1, 'Feature'),
    (2, 'Task'),
    (3, 'User Story'),
)



class Issue(models.Model):
    title = models.CharField(max_length=100, blank=False, default='')
    slug = models.SlugField(max_length=100, unique=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='issues'
    )
    description = models.TextField(blank=False, default='')
    status = models.IntegerField(choices=ISSUE_STATUS, default=0)
    priority = models.IntegerField(choices=ISSUE_PRIORITY, default=0)
    type = models.IntegerField(choices=ISSUE_TYPE, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    votes = models.ManyToManyField(User, related_name='votes', blank=True)
    
    class Meta:
        ordering = ['priority', '-created_on', 'status']

    def __str__(self):
        return self.title
    
    def votes_number(self):
        return self.votes.count()
    

class Comment(models.Model):
    issue = models.ForeignKey(
        Issue,
        on_delete=models.CASCADE,
        related_name='comments',
        blank=False,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    comment = models.TextField(blank=False, default='')
    created_on = models.DateTimeField(auto_now_add=True, blank=False, editable=False)
    updated_on = models.DateTimeField(auto_now=True, blank=False, editable=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.comment


class Project(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    slug = models.SlugField(max_length=100, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dev_projects')
    description = models.TextField(blank=False, default='')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    issues = models.ManyToManyField(Issue, related_name='projects', blank=True)
    members = models.ManyToManyField(User, related_name='projects', blank=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    related_projects = models.ManyToManyField(Project, related_name='related_projects', blank=True)
    assigned_issues = models.ManyToManyField(Issue, related_name='assigned_issues', blank=True)
