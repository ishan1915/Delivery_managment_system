# --- utils.py (optional helper to assign role) ---
from rolepermissions.roles import assign_role

def assign_user_role(user, role_name):
    assign_role(user, role_name)