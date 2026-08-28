# Amana Suite Admin Panel Mandatory Setup & Configuration Guide

## 1. Environment Variables Setup (`/www/wwwroot/amanasuite.com/.env`)
Ensure the following core host and IP environment variables are configured in `.env`:

```env
APP_HOST_DOMAIN=amanasuite.com
APP_HOST_BASE_DOMAIN=amanamart.com
APP_PUBLIC_IP=148.230.98.190

APP_URL=https://amanasuite.com
```

- **`APP_HOST_DOMAIN`:** Backend API and Admin Panel host (`amanasuite.com`).
- **`APP_HOST_BASE_DOMAIN`:** Customer Web Portal base domain (`amanamart.com`).
- **`APP_PUBLIC_IP`:** Server Public IP (`148.230.98.190`).

---

## 2. Business Setup & White-Labeling
Navigate to **Admin Panel > Business Settings > Business Setup**:
- **App Name:** `Amana Mart`
- **Company Name:** `Amana Mart Limited`
- **Timezone:** `Asia/Dhaka` (GMT+6)
- **Currency:** BDT (`৳` Taka)
- **Logos:** Upload Amana Mart 512x512 PNG/WEBP Logo & Favicon.
- **Time Format:** 12 Hour (`hh:mm a`)

---

## 3. Google Maps API Configuration
Navigate to **Admin Panel > 3rd Party APIs > Map API Setup**:
- **Client Map API Key:** Google Maps JavaScript API Key (restricted to `amanamart.com` and `amanasuite.com`).
- **Server Map API Key:** Google Maps Geocoding & Places API Key (restricted to Server IP `148.230.98.190`).

---

## 4. Firebase FCM Push Notification Setup
Firebase handles real-time push notifications for order placement, driver tracking, and chat messages.

### A. Service Account Key
1. Open [Firebase Console](https://console.firebase.google.com/) > Select Project > **Project Settings** > **Service Accounts**.
2. Click **Generate New Private Key** to download the JSON file.
3. Open Admin Panel > **3rd Party > Push Notification > Firebase Configuration**.
4. Paste the entire contents of the Firebase Service Account JSON file into the **Service File Content** field and save.

### B. Service Worker (`firebase-messaging-sw.js`)
For Web Push Notifications on `amanamart.com`, place `firebase-messaging-sw.js` in `/www/wwwroot/amanamart/public/`:
```javascript
importScripts('https://www.gstatic.com/firebasejs/9.0.0/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/9.0.0/firebase-messaging-compat.js');

firebase.initializeApp({
  apiKey: "YOUR_FIREBASE_API_KEY",
  authDomain: "amana-mart.firebaseapp.com",
  projectId: "amana-mart",
  storageBucket: "amana-mart.appspot.com",
  messagingSenderId: "YOUR_SENDER_ID",
  appId: "YOUR_APP_ID"
});

const messaging = firebase.messaging();
```

---

## 5. SMTP Mail Configuration
Navigate to **Admin Panel > 3rd Party > Mail Config**:
- **Mailer:** `smtp`
- **Host:** `mail.amanamart.com` / `smtp.gmail.com`
- **Port:** `587` (TLS) / `465` (SSL)
- **Username:** `info@amanamart.com`
- **Encryption:** `tls` / `ssl`

---

## 6. Payment & SMS Gateway Configuration
- **Digital Payment Gateways:** SSLCOMMERZ, Bkash, Nagad, Stripe, Cash on Delivery.
- **OTP SMS Gateways:** SMS API for OTP customer verification during signup and password recovery.
