from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('warehouse_manager', 'Warehouse Manager'),
        ('city_manager', 'City Manager'),
        ('porter', 'Porter'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    def save(self, *args, **kwargs):
        # If setting a raw password manually, hash it
        if self.pk is None:  # When creating a new user
            self.set_password(self.password)
        else:
            old = User.objects.filter(pk=self.pk).first()
            if old and old.password != self.password:
                self.set_password(self.password)
        super().save(*args, **kwargs)