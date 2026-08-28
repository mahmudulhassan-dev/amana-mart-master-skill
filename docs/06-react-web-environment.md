# Amana Mart React / Next.js Web Portal — Environment & Admin Setup Guide

## 1. Next.js Production Environment Setup (`/www/wwwroot/amanamart/.env.production`)

Configure the environment variables in `/www/wwwroot/amanamart/.env.production`:

```env
NEXT_PUBLIC_BASE_URL="https://amanasuite.com"
NEXT_PUBLIC_APP_NAME="Amana Mart"
NEXT_PUBLIC_WEB_HOST="https://amanamart.com"
```

*(CRITICAL WARNING: Do NOT put a trailing slash `/` at the end of `NEXT_PUBLIC_BASE_URL`, or API fetches will result in double slashes e.g. `amanasuite.com//api/v1` and throw 404 errors).*

---

## 2. Admin Panel Configuration (`https://amanasuite.com`)

### A. React Web Add-on Activation
1. Log in to **Amana Suite Admin Panel** at `https://amanasuite.com/login/admin`.
2. Open **Business Settings > System Settings > System Add-ons**.
3. Toggle **React Web Portal** to **Active**.

### B. Landing Page & Header Customization
1. Open **Admin Panel > Settings > Pages & Social Media > React Landing Page**.
2. Configure Amana Mart brand headers:
   - **Header Title:** `Amana Mart — Hyperlocal Marketplace & Delivery`
   - **Subtitle:** `Order Food, Grocery, Pharmacy, Parcels, and Rent Vehicles in One App`
   - **Social Links:** Facebook, Twitter, Instagram, YouTube URLs.
   - **Footer Articles:** Terms & Conditions, Privacy Policy, About Amana Mart.

---

## 3. Verifying Node & Web Server Connection
Run a connection test from the web portal directory to the admin API:

```bash
cd /www/wwwroot/amanamart
curl -s -I https://amanasuite.com/api/v1/config
```
Expected output: `HTTP/1.1 200 OK`.
