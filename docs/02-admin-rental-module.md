# Amana Suite Car Rental & Ride-Share Module Installation Guide

## 1. Module Overview
The **Amana Mart Car Rental & Ride-Share Module** extends the ecosystem to support vehicle booking, hourly/daily car rentals, driver dispatching, distance-based trip fares, and vehicle fleet management.

---

## 2. Step-by-Step Module Installation & Activation

### Step 1: Upload Module Add-on Zip
1. Log in to **Amana Suite Admin Panel** at `https://amanasuite.com/login/admin`.
2. Navigate to **Business Settings > System Settings > System Add-ons**.
3. Click **Upload Add-on** and select the Car Rental Module zip package.

### Step 2: Activate Module
On the **System Add-ons** list, locate the **Car Rental & Ride-Share Module** and toggle the status to **Active**.

### Step 3: Module Configuration
1. **Admin Panel Setup:**
   - Configure vehicle categories (Sedan, SUV, Microbus, Bike, Luxury).
   - Set fare structure: Base fare, Per-KM rate, Hourly rate, Driver allowance.
   - Set commission percentage for rental providers and individual drivers.
2. **Web & App Integration:**
   - The rental module automatically exposes API endpoints under `/api/v1/rental/` for `amanamart.com` and `amanamartuserapp`.
