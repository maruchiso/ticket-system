from django.db import models
from django.contrib.auth.models import AbstractUser, User

class CustomUser(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )

    role = models.CharField(max_length=10, choices=ROLES, default='user')
      
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_groups",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        verbose_name="groups",
    )
    
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_user_permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

class Zgloszenie(models.Model):
    STATUS_CHOICES = [
        ('NEW', 'Nowe'),
        ('OPEN', 'Otwarte'),
        ('CLOSE', 'Zamkniete'),
    ]
    PRIORITY_CHOICES = [
        ('P1', 'P1'),
        ('P2', 'P2'),
        ('P3', 'P3'),
        ('P4', 'P4'),
        ('P5', 'P5'),

    ]
    
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    priority = models.CharField(max_length=2, choices=PRIORITY_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title