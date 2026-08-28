# Amana Mart React Web Portal — Car Rental & Ride Addon Integration Guide

## 1. Overview of Web Rental Module
The **Car Rental & Ride Booking Web Module** integrates vehicle fleet search, hourly/daily car booking, map pickup/drop selection, and driver hire directly into the **Amana Mart** customer web portal (`amanamart.com`).

---

## 2. Step-by-Step Module Integration in Next.js Project

### Step 1: Locate Component Directory
Navigate to the web portal component directory:
- **Directory Path:** `/www/wwwroot/amanamart/src/components/home/module-wise-components/`

### Step 2: Embed Rental Component Code
Replace any legacy empty `rental` placeholder with the full React rental module component:
- **Module Component Path:** `/www/wwwroot/amanamart/src/components/home/module-wise-components/rental`

### Step 3: Rebuild Next.js Web App
Recompile production assets and restart PM2:

```bash
cd /www/wwwroot/amanamart
npm run build
pm2 restart amanamart
```

---

## 3. Web Car Rental UI Functionality
Once integrated, visiting `https://amanamart.com` and clicking the **Car Rental & Ride** module tab loads:
- **Location Selector:** Google Maps Places autocomplete for Pickup & Destination.
- **Vehicle Fleet Filter:** Sedan, SUV, Microbus, Bike, Luxury filter tabs.
- **Trip Estimation:** Instant fare calculation powered by `https://amanasuite.com/api/v1/rental/`.
