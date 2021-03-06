from django.db import models
from django.contrib.auth.models import User

DEFAULT_PROJECT_ID = 1

# project model variables
PROJECT_TYPE = (
    (0, 'Personal Project'),
    (1, 'Team Project'),
)

PROJECT_STATUS = (
    (0, 'In Progress'),
    (1, 'Completed'),
)

# issue model variables
ISSUE_STATUS = (
    (0, 'Open'),
    (1, 'In Progress'),
    (2, 'Closed'),
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


class Project(models.Model):
    title = models.CharField(
        max_length=35,
        blank=False,
        default='Untitled Project'
        )
    # slug = models.SlugField(max_length=100, blank=False)
    description = models.TextField(max_length=300, blank=True)
    project_type = models.IntegerField(choices=PROJECT_TYPE)
    status = models.IntegerField(choices=PROJECT_STATUS, default=0)
    collaborators = models.ManyToManyField(
        User,
        related_name='collaborated_projects'
        )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='projects',
        null=True
        )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Issue(models.Model):
    title = models.CharField(max_length=35, blank=False, default='')
    # slug = models.SlugField(max_length=100)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='issues'
    )
    description = models.TextField(max_length=300, blank=False, default='')
    status = models.IntegerField(choices=ISSUE_STATUS, default=0)
    priority = models.IntegerField(choices=ISSUE_PRIORITY, default=0)
    issue_type = models.IntegerField(choices=ISSUE_TYPE, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    votes = models.ManyToManyField(
        User,
        related_name='voted_on_issue',
        blank=True
        )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='issues',
        default=DEFAULT_PROJECT_ID
        )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='assigned_issues'
    )

    class Meta:
        ordering = ['priority', 'status']

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
        related_name='written_comments',
    )
    comment_body = models.TextField(max_length=300, blank=False, default='')
    created_on = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        editable=False
        )
    updated_on = models.DateTimeField(
        auto_now=True,
        blank=False,
        editable=False
        )

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.comment_body
