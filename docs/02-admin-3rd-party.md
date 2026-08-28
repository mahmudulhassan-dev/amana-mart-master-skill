# Amana Suite Laravel Reverb Real-Time WebSockets & 3rd Party Setup

## 1. Real-Time WebSockets Architecture (Laravel Reverb)
**Amana Suite** utilizes **Laravel Reverb** as its primary real-time WebSocket server for instant driver location tracking, live customer order status updates, and in-app chat notifications.

---

## 2. Environment Configuration (`/www/wwwroot/amanasuite.com/.env`)

Add the following Reverb & Pusher compatibility variables to `.env`:

```env
# Primary Reverb Broadcasting Configuration
BROADCAST_DRIVER=reverb

REVERB_APP_ID=amanasuite
REVERB_APP_KEY=amanasuite_key_2026
REVERB_APP_SECRET=amanasuite_secret_2026
REVERB_HOST=amanasuite.com
REVERB_PORT=6001
REVERB_SCHEME=https

# Client-Side Pusher Compatibility
PUSHER_APP_ID=amanasuite
PUSHER_APP_KEY=amanasuite_key_2026
PUSHER_APP_SECRET=amanasuite_secret_2026
PUSHER_HOST=amanasuite.com
PUSHER_PORT=6001
PUSHER_SCHEME=https
PUSHER_APP_CLUSTER=mt1
```

---

## 3. Process Management (PM2 & Supervisor Execution)

To keep Laravel Reverb running 24/7 on port 6001:

### PM2 Command:
```bash
cd /www/wwwroot/amanasuite.com
pm2 start "php artisan reverb:start --host=0.0.0.0 --port=6001" --name "amanasuite-reverb"
```

### Laravel Queue Worker PM2 Command:
```bash
cd /www/wwwroot/amanasuite.com
pm2 start "php artisan queue:work --tries=3" --name "amanasuite-queue"
```

---

## 4. Admin Panel WebSocket Configuration
1. Open **Admin Panel > 3rd Party & Configuration > WebSocket Settings**.
2. **Enable WebSocket:** Toggle **ON**.
3. **WebSocket Host:** `amanasuite.com`
4. **WebSocket Port:** `6001`
5. **SSL Scheme:** `https`

Click **Save & Apply**. Real-time driver maps and live order updates are now active across all mobile apps and web!
