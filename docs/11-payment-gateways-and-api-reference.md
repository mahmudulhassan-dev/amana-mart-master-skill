# Amana Mart Ecosystem — Payment Gateways & REST API Reference Guide

## 1. Local & International Payment Gateways Integration

**Amana Suite** (`amanasuite.com`) includes native digital payment gateways for customer checkout across the mobile apps and web portal:

### A. Local Bangladesh Payment Gateways
1. **SSLCOMMERZ (Cards & Mobile Banking):**
   - Admin Panel > **3rd Party > Payment Methods > SSLCOMMERZ**.
   - Configuration: Store ID, Store Password, Sandbox / Live Mode.
2. **Bkash Direct Payment:**
   - Admin Panel > **Payment Methods > Bkash**.
   - Configuration: App Key, App Secret, Username, Password.
3. **Nagad Direct Payment:**
   - Admin Panel > **Payment Methods > Nagad**.
   - Configuration: Merchant ID, Public Key, Private Key.

### B. International Payment Gateways
1. **Stripe (Credit / Debit Cards):**
   - Configuration: Publishable Key, Secret Key.
2. **PayPal:**
   - Configuration: Client ID, Secret Key.
3. **Cash on Delivery (COD):**
   - Configurable per zone and order amount limit.

---

## 2. Core REST API Endpoints Overview (`https://amanasuite.com/api/v1/`)

All API requests require the `X-localization: bn` header for Bengali content and `Authorization: Bearer <TOKEN>` for authenticated routes.

| Module | HTTP Method | API Endpoint | Description |
| :--- | :--- | :--- | :--- |
| **Config** | `GET` | `/api/v1/config` | System settings, base URLs, modules & minimum app versions |
| **Auth** | `POST` | `/api/v1/auth/login` | Customer / Driver / Vendor login with phone/email |
| **Stores** | `GET` | `/api/v1/stores/get-stores/all` | List nearby stores by zone and geolocation |
| **Items** | `GET` | `/api/v1/items/latest` | Browse products, food items, groceries & medicines |
| **Orders** | `POST` | `/api/v1/customer/order/place` | Place new order with payment gateway & coupon |
| **Tracking** | `GET` | `/api/v1/customer/order/track?order_id=X` | Real-time order status and driver GPS coordinates |
| **Rental** | `GET` | `/api/v1/rental/vehicles` | Browse available rental cars and calculate trip fare |
