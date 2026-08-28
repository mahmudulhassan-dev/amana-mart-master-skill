# Amana Mart Vendor Website Builder & Custom Subdomain Guide

## 1. Feature Overview
The **Amana Mart Vendor Website Builder Add-on** allows individual store merchants to automatically generate and publish their own branded online storefront (e.g., `storename.amanamart.com` or custom domain `www.merchantsite.com`) powered by Amana Suite.

---

## 2. Activation Steps (Admin & Merchant Panel)

### Step 1: Upload & Activate Add-on
1. Log in to **Amana Suite Admin Panel** at `https://amanasuite.com/login/admin`.
2. Open **Business Settings > System Settings > System Add-ons**.
3. Upload the **Vendor Website Builder Add-on** zip and click **Activate**.

### Step 2: Enable Feature in Admin Settings
1. Open **Business Settings > Vendor Website Builder**.
2. Toggle **Enable Website Builder** to **ON**.

### Step 3: Enable Feature in Store Merchant Panel
1. Merchant logs in to **Store Panel** at `https://amanasuite.com/login/store`.
2. Open **Store Config > Website Builder**.
3. Toggle **Enable Store Website** to **ON**.

---

## 3. Mandatory Wildcard Subdomain Configuration

To allow merchants to launch subdomains (`store1.amanamart.com`, `fashion.amanamart.com`) automatically without manual DNS edits, configure a Wildcard A Record.

### A. Cloudflare / DNS Settings
Add a wildcard A record in your DNS manager:
- **Type:** `A`
- **Name / Host:** `*`
- **IPv4 Address:** `148.230.98.190` (Amana Server Public IP)
- **TTL:** Auto

### B. Nginx Wildcard Configuration
In `/www/server/panel/vhost/nginx/amanamart.com.conf`:
```nginx
server {
    listen 80;
    listen 443 ssl http2;
    server_name amanamart.com *.amanamart.com;
    # ...
}
```

---

## 4. Merchant Custom Domain Setup

If a store merchant wishes to connect their own independent domain (e.g. `www.myshop.com`):
1. **Merchant DNS Setup:** Merchant sets an `A` record pointing `@` and `www` to Amana Server IP `148.230.98.190`.
2. **Admin Verification:** In Admin Panel > **Vendor Websites > Custom Domains**, verify DNS propagation and approve domain binding.
