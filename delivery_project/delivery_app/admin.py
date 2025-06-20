from django.contrib import admin
from .models import User,CityManager,Customer,Porter,Order,WarehouseManager
# Register your models here.
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Porter)
admin.site.register(CityManager)
admin.site.register(Order)
admin.site.register(WarehouseManager)




 