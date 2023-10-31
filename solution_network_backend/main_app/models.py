from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Problem(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Solution(models.Model):
    problem = models.ForeignKey(Problem, related_name='solutions', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Solution for {self.problem.title}'

class User(AbstractUser):
    # Your custom fields here

    # Add related_name to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name="custom_user_set",
        related_query_name="user",
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_set",
        related_query_name="user",
        verbose_name='user permissions'
    )
