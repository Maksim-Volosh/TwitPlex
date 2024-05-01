from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(
        max_length=30,
        verbose_name="Name"
    )
    
    bio = models.TextField(
        blank=True,
        verbose_name="Bio",
        max_length=80
    )
    
    sphere = models.CharField(
        blank=True,
        max_length=35,
        verbose_name="Sphere"
    )
    
    image = models.ImageField(
        upload_to='users_images',
        blank=True,
        null=True,
        verbose_name="Avatar"
    )

    class Meta:
        db_table = "user"
        verbose_name = "User"
        verbose_name_plural = "Users"
        
    def __str__(self):
        return self.username
