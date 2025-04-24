from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    # Ensure that reverse accessors are unique by adding a `related_name`
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Adding a custom related_name
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Adding a custom related_name
        blank=True
    )
    
    # You can add other custom fields here if necessary
