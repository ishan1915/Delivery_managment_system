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
    def save(self, *args, **kwargs):                             #for creating   hashed password when user created from admin panel
        # If setting a raw password manually, hash it
        if self.pk is None:  # When creating a new user
            self.set_password(self.password)
        else:
            old = User.objects.filter(pk=self.pk).first()
            if old and old.password != self.password:
                self.set_password(self.password)
        super().save(*args, **kwargs)


class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)    
    address=models.TextField()
    phone=models.CharField(max_length=10)
    city=models.CharField(max_length=100)
    pincode=models.CharField(max_length=10)   


    def __str__(self):
        return f"{self.user} {self.address}"

    

class WarehouseManager(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    warehouse_name=models.CharField(max_length=255)
    location=models.CharField(max_length=255)


    def __str__(self):
        return f"{self.user} {self.location}"

class CityManager(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    city=models.CharField(max_length=100)


    def __str__(self):
        return f"{self.user} {self.city}"


class Porter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    assigned_area = models.CharField(max_length=10)


    def __str__(self):
        return f"{self.user} {self.assigned_area}"

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    price=models.IntegerField()

    warehouse_manager = models.ForeignKey(WarehouseManager, on_delete=models.SET_NULL, null=True, blank=True)
    city_manager = models.ForeignKey(CityManager, on_delete=models.SET_NULL, null=True, blank=True)
    porter = models.ForeignKey(Porter, on_delete=models.SET_NULL, null=True, blank=True)

    is_packed = models.BooleanField(default=False)
    is_shipped = models.BooleanField(default=False)
    received_at_city = models.BooleanField(default=False)
    out_for_delivery = models.BooleanField(default=False)

    is_delivered = models.BooleanField(default=False)            


    def __str__(self):
        return f"{self.customer} "
    


class DeliveryArea(models.Model):
    pincode = models.CharField(max_length=6)
    porter = models.ForeignKey(Porter, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pincode} - {self.porter.user.username}"    