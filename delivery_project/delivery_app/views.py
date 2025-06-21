from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login,logout
from .models import *
from .forms import *
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from rolepermissions.checkers import has_permission

def user_login(request):
    error = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(f'{user.role}_dashboard')
        else:
            error = "Invalid credentials"
    return render(request, 'login.html', {'error': error})

def custom_logout(request):
    logout(request)
    return redirect('login')


def signup_customer(request):
    form = CustomerSignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('customer_dashboard')
    return render(request, 'signup.html', {'form': form, 'role': 'Customer'})


@login_required
def customer_dashboard(request):
    orders=Order.objects.filter(customer=request.user.customer)
    return render(request,'customer_dashboard.html',{'orders':orders})

@login_required
def customer_history(request):
    #customer = request.user.customer
    orders = Order.objects.filter(customer=request.user.customer, is_delivered=True).order_by('-created_at')
    return render(request, 'customer_history.html', {'orders': orders})

@login_required 
def mark_order_delivered(request,order_id):
    order=get_object_or_404(Order,id=order_id,customer=request.user.customer)
    order.is_delivered=True
    order.save()
    return redirect('customer_dashboard')

def create_order(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        customer = request.user.customer
        order = form.save(commit=False)
        order.customer = customer
        order.city_manager = CityManager.objects.filter(city=customer.city).first()
        order.warehouse_manager = WarehouseManager.objects.filter(location__icontains=customer.city).first()
        order.porter = Porter.objects.filter(assigned_area=customer.pincode).first()
        order.save()
        return redirect('customer_dashboard')
    return render(request, 'create_order.html', {'form': form})




def warehouse_manager_dashboard(request):
    wm = request.user.warehousemanager
    orders = Order.objects.filter(warehouse_manager=wm)
    return render(request, 'warehouse_dashboard.html', {'orders': orders})

def city_manager_dashboard(request):
    cm = request.user.citymanager
    orders = Order.objects.filter(city_manager=cm)
    return render(request, 'city_dashboard.html', {'orders': orders})

def porter_dashboard(request):
    p = request.user.porter
    orders = Order.objects.filter(porter=p)
    return render(request, 'porter_dashboard.html', {'orders': orders})



# Warehouse Manager updates
@require_POST
def mark_packed(request, order_id):
    if not has_permission(request.user, 'mark_packed'):
        return HttpResponseForbidden("Not allowed")
    order = get_object_or_404(Order, id=order_id, warehouse_manager=request.user.warehousemanager)
    order.is_packed = True
    order.save()
    return redirect('warehouse_manager_dashboard')

@require_POST
def mark_shipped(request, order_id):
    order = get_object_or_404(Order, id=order_id, warehouse_manager=request.user.warehousemanager)
    order.is_shipped = True
    order.save()
    return redirect('warehouse_manager_dashboard')

# City Manager updates
@require_POST
def mark_received_city(request, order_id):
    order = get_object_or_404(Order, id=order_id, city_manager=request.user.citymanager)
    order.received_at_city = True
    order.save()
    return redirect('city_manager_dashboard')

# Porter updates
@require_POST
def mark_out_for_delivery(request, order_id):
    order = get_object_or_404(Order, id=order_id, porter=request.user.porter)
    order.out_for_delivery = True
    order.save()
    return redirect('porter_dashboard')
