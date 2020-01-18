from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserInfo(models.Model):
    """
    Model For Additional User info
    """

    CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = "userInfo")
    age  = models.IntegerField()
    have_siblings = models.CharField(max_length=3, choices=CHOICES, default="No")
    known_env_exposures = models.CharField(max_length=30)
    known_genetic_mutations = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.user.first_name} Profile"
