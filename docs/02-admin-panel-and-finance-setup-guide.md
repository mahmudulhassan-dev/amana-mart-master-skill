# Amana Mart Admin Panel & Finance Setup Guide

## 1. Server Environment & Prerequisites
- **Web Server:** Nginx / Apache with SSL
- **PHP Version:** PHP 8.2 or 8.3 with required extensions:
  - `bcmath`, `ctype`, `curl`, `fileinfo`, `json`, `mbstring`, `openssl`, `pdo_mysql`, `tokenizer`, `xml`, `zip`, `gd`
- **Database:** MySQL 8.0 or MariaDB 10.6+

## 2. Directory & Environment Setup
- **Server Path:** `/www/wwwroot/amanasuite.com`
- **Environment File:** `/www/wwwroot/amanasuite.com/.env`

### Core Environment Parameters
```env
APP_NAME="Amana Suite"
APP_ENV=production
APP_DEBUG=false
APP_URL=https://amanasuite.com

DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=amanasuite
DB_USERNAME=amanasuite
DB_PASSWORD=your_secure_password

BROADCAST_DRIVER=pusher
QUEUE_CONNECTION=database
CACHE_DRIVER=file
```

## 3. Financial & Business Settings
1. **Commission Setup:** Admin Panel > Business Settings > Business Setup > Default Admin Commission.
2. **Withdrawal Methods:** Admin Panel > Business Settings > Withdrawal Methods (Bank Transfer, Mobile Banking).
3. **Delivery Fees:** Fixed vs Distance-based delivery fee per zone.
4. **Tax & VAT:** Included or Excluded VAT/Tax calculations per store module.

## 4. Automated Cron Job Configuration
Add to server crontab (`crontab -e`):
```bash
* * * * * cd /www/wwwroot/amanasuite.com && php artisan schedule:run >> /dev/null 2>&1
```
