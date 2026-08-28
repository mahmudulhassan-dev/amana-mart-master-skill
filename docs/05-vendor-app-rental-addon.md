# Amana Mart Store Merchant App — Rental & Fleet Module Integration Guide

## 1. Overview of Merchant Rental Fleet Management
Vehicle rental providers and fleet operators manage their car inventories, driver assignments, hourly rental pricing, and vehicle maintenance status directly from the **Amana Mart Store Merchant App** (`amanamartvendorapp`).

---

## 2. Step-by-Step Module Integration in Merchant App

### Step 1: Remove Obsolete Taxi Stubs
Navigate to merchant app features directory and remove legacy taxi stubs:
```bash
cd /www/wwwroot/amanamartvendorapp
rm -rf lib/features/taxi_module
```

### Step 2: Clean Flutter Build Cache
Clear compiled cache to avoid duplicate class conflicts:
```bash
/opt/flutter/bin/flutter pub cache clean -f
/opt/flutter/bin/flutter clean
```

### Step 3: Embed Rental Module Source Code
Place the `rental_module` package inside the features directory:
- **Module Path:** `/www/wwwroot/amanamartvendorapp/lib/features/rental_module`

### Step 4: Resolve Dependencies & Build Merchant App
```bash
export ANDROID_HOME=/opt/android-sdk
cd /www/wwwroot/amanamartvendorapp
/opt/flutter/bin/flutter pub get
/opt/flutter/bin/flutter build apk --release
```

---

## 3. Merchant Fleet Dashboard
When `rental_module` is active, vehicle providers access dedicated fleet management tools:
- **Vehicle Inventory:** Add new cars, SUVs, Microbuses with license plate, seating capacity, and driver assignment.
- **Trip Bookings:** View incoming hourly and distance-based trip requests with live map tracking.
- **Fleet Earnings:** Payout requests and trip commission summaries.
