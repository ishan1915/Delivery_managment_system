 
 
---

## 📦 Delivery Management System - Django Based

A multi-role delivery management system built with Django where **Customers**, **Warehouse Managers**, **City Managers**, and **Porters** interact to handle package deliveries from order creation to final delivery.

---

## 🚀 Features

### ✅ User Roles

* **Customer**

  * Register and login
  * Create new orders
  * View live status of orders via progress tracker
  * Mark orders as delivered
  * View complete delivery history
  * Download PDF invoice
  * Edit personal profile

* **Warehouse Manager**

  * Assigned by Admin
  * View all assigned orders
  * Mark order as `Packed` and `Shipped`

* **City Manager**

  * Assigned by Admin
  * View all shipped orders in their city
  * Mark orders as `Received at City Office`

* **Porter**

  * Assigned by Admin
  * View all orders in their assigned pincode
  * Mark orders as `Out for Delivery`

* **Admin (via Django Admin Panel)**

  * Create and assign Warehouse Managers, City Managers, Porters
  * Assign pincodes and cities
  * Reassign orders manually (coming soon)
  * Monitor all deliveries

---

## 📄 Major Functionalities

### 🛒 Order Management

* Order is routed automatically to correct:

  * Warehouse Manager (by customer city)
  * City Manager (by city)
  * Porter (by matching pincode)
* Admin panel can reassign staff manually (optional future feature)

### 📈 Progress Tracker

* Each order has a **visual progress bar** with:

  * ✅ Packed
  * ✅ Shipped
  * ✅ Received at City Office
  * ✅ Out for Delivery
  * ✅ Delivered

### 🧾 Invoice PDF

* Generates invoice using `WeasyPrint`
* PDF includes customer, product, and delivery status

### 📋 Profile Management

* Customers can:

  * Edit their address, phone, city, and pincode
* Admin manages other roles

### 📜 Order History

* Delivered orders with full tracking and timestamps
* Downloadable invoices

---

## 🛠️ Tech Stack

* **Backend**: Django (with custom user model)
* **Frontend**: HTML, CSS (custom), Django Templates
* **Permissions**: `django-role-permissions`
* **PDF Generation**: `WeasyPrint`
* **Session-based Auth**: Django built-in

---

## ⚙️ Setup Instructions

1. **Clone the repo**

   ```bash
   git clone https://github.com/yourusername/delivery-management.git
   cd delivery-management
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **Start the server**

   ```bash
   python manage.py runserver
   ```

---

## 🧪 Sample Users

| Role     | Username | Password | Notes                   |
| -------- | -------- | -------- | ----------------------- |
| Admin    | admin    | admin123 | Full control via /admin |
| Customer | testuser | testpass | Can create/view orders  |

---

## 📝 Future Enhancements

* 🔔 Email or SMS notifications (e.g., via Twilio)
* 📍 Google Maps for porter routes
* 📊 Analytics Dashboard for Admin
* 📦 Bulk order CSV upload
* 🔁 Manual reassignment with drag-and-drop (via JS)
* 🌐 REST API + React frontend
* 📱 Android APK (WebView/Flutter)

---

 
 
---
 
