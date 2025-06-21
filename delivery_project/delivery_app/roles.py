
from rolepermissions.roles import AbstractUserRole

class Customer(AbstractUserRole):
    available_permissions = {
        'create_order': True,
    }

class WarehouseManager(AbstractUserRole):
    available_permissions = {
        'mark_packed': True,
        'mark_shipped': True,
    }

class CityManager(AbstractUserRole):
    available_permissions = {
        'mark_received_at_city': True,
    }

class Porter(AbstractUserRole):
    available_permissions = {
        'mark_out_for_delivery': True,
        'mark_delivered': True,
    }

