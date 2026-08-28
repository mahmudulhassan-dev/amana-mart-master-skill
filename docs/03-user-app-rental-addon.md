# Amana Mart Customer User App — Car Rental & Ride Addon Integration Guide

## 1. Overview of Mobile Rental Integration
The **Car Rental & Ride Booking Module** allows customers to select vehicles (Sedan, SUV, Microbus, Luxury), choose hourly or daily trip rentals, select pickup & drop locations on Google Maps, and hire drivers directly from the **Amana Mart** mobile application.

---

## 2. Step-by-Step Module Integration in Flutter App

### Step 1: Remove Legacy Taxi Module
Navigate to the customer app features folder and remove obsolete taxi stubs:
```bash
cd /www/wwwroot/amanamartuserapp
rm -rf lib/features/taxi_module
```

### Step 2: Clean Flutter Build Cache
Clear compiled cache to prevent duplicate class conflicts:
```bash
/opt/flutter/bin/flutter pub cache clean -f
/opt/flutter/bin/flutter clean
```

### Step 3: Embed Rental Module Source Code
Place the `rental_module` package inside the features directory:
- **Module Path:** `/www/wwwroot/amanamartuserapp/lib/features/rental_module`

### Step 4: Resolve Dependencies & Rebuild App
```bash
export ANDROID_HOME=/opt/android-sdk
cd /www/wwwroot/amanamartuserapp
/opt/flutter/bin/flutter pub get
/opt/flutter/bin/flutter build apk --release
```

---

## 3. Verifying Module Active Status
1. When `rental_module` is active, the app home screen automatically displays the **"Car Rental & Ride"** module icon alongside Food, Grocery, Pharmacy, and Parcel.
2. Selecting the Ride icon opens Google Maps pickup/drop location selection and vehicle fleet options connected to `https://amanasuite.com/api/v1/rental/`.
