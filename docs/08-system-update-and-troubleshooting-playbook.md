# Amana Mart Ecosystem — Performance Optimization & Troubleshooting Playbook

## 1. System Performance & High-Speed Caching Setup

To maintain lightning-fast response times (< 200ms) across **Amana Suite** (`amanasuite.com`), **Amana Mart Web** (`amanamart.com`), and the 3 mobile apps:

### A. Redis Database Caching (`/www/wwwroot/amanasuite.com/.env`)
Set Redis as the primary cache and session driver in Laravel:
```env
CACHE_DRIVER=redis
SESSION_DRIVER=redis
QUEUE_CONNECTION=database
```

### B. Nginx Static Asset Caching (`amanamart.com.conf`)
Enable gzip compression and browser caching in Nginx:
```nginx
location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg|woff|woff2|ttf|eot)$ {
    expires 30d;
    add_header Cache-Control "public, no-transform";
}
```

---

## 2. Typical Production Issues & Step-by-Step Fixes

### Issue 1: Web Portal Text Stays in English When Switching to Bengali
- **Root Cause:** Missing or untranslated keys in `src/language/bn.js`.
- **Solution:** Ensure all 2,522 keys in `/www/wwwroot/amanamart/src/language/bn.js` are translated into Bengali, then run `npm run build && pm2 restart amanamart`.

### Issue 2: Flutter Release APK Fails on Gradle OOM (OutOfMemoryError)
- **Root Cause:** Gradle daemon attempting to allocate 8GB heap memory.
- **Solution:** Set `org.gradle.jvmargs=-Xmx3072m -XX:MaxMetaspaceSize=1024m` in `android/gradle.properties`.

### Issue 3: Server Disk Full (100% Used)
- **Root Cause:** Uncapped system log files (`/var/log/syslog`, `/var/log/mail.log`) growing > 100GB.
- **Solution:** Run the automated maintenance script `/root/amana-mart-master-skill/scripts/server-maintenance.sh`.

### Issue 4: Google Maps Shows Blank or "For Development Purposes Only"
- **Root Cause:** Missing billing account or Routes/Places API (New) unenabled in Google Cloud Console.
- **Solution:** Enable **Routes API** and **Places API (New)** in Google Cloud Console and ensure billing status is Active.
