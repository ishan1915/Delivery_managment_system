from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.custom_logout,name='logout'),
    path('signup/', views.signup_customer, name='signup_customer'),
    path('customer_dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('edit_profile/',views.edit_customer_profile, name='edit_customer_profile'),


    path('customer_history/',views.customer_history,name='customer_history'),
    path('order/<int:order_id>/delivered/', views.mark_order_delivered, name='mark_order_delivered'),

    path('order_create/', views.create_order, name='create_order'),

    path('warehouse_dashboard/', views.warehouse_manager_dashboard, name='warehouse_manager_dashboard'),
    path('edit_wmprofile/',views.edit_wm_profile, name='edit_wm_profile'),



    path('city_dashboard/', views.city_manager_dashboard, name='city_manager_dashboard'),
    path('porter_dashboard/', views.porter_dashboard, name='porter_dashboard'),

   # Warehouse Manager
    path('order/<int:order_id>/pack/', views.mark_packed, name='mark_packed'),
    path('order/<int:order_id>/ship/', views.mark_shipped, name='mark_shipped'),

    # City Manager
    path('order/<int:order_id>/receive_city/', views.mark_received_city, name='mark_received_city'),

     # Porter
     path('order/<int:order_id>/out_for_delivery/', views.mark_out_for_delivery, name='mark_out_for_delivery'),
   
     path('invoice/<int:order_id>/', views.generate_invoice, name='generate_invoice'),


      # Password Change
    path('password_change/',
         auth_views.PasswordChangeView.as_view(template_name='auth/password_change.html'),
         name='password_change'),

    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='auth/password_change_done.html'),
         name='password_change_done'),

    # Password Reset
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='auth/password_reset.html'),
         name='password_reset'),

    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='auth/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='auth/password_reset_complete.html'),
         name='password_reset_complete'),



]
