# Amana Suite Backend Environment & Server Configuration Guide

## 1. Domain & Server Architecture Specifications
For the **Amana Mart Ecosystem**, a dual-domain setup is implemented:
- **Central Backend API & Admin Panel (`https://amanasuite.com`):** Hosted at `/www/wwwroot/amanasuite.com`. Acts as the primary API host for mobile apps and web.
- **Customer Web Portal (`https://amanamart.com`):** Hosted at `/www/wwwroot/amanamart`. Next.js 15 customer web app.

---

## 2. Server Infrastructure (Ubuntu 24.04 & aaPanel / Nginx)

### A. Web Server & Virtual Host (Nginx)
The virtual host block for `amanasuite.com` at `/www/server/panel/vhost/nginx/amanasuite.com.conf`:
```nginx
server {
    listen 80;
    listen 443 ssl http2;
    server_name amanasuite.com www.amanasuite.com;
    root /www/wwwroot/amanasuite.com/public;
    index index.php index.html;

    client_max_body_size 128M;

    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }

    location ~ \.php$ {
        fastcgi_pass unix:/tmp/php-cgi-82.sock;
        fastcgi_index index.php;
        include fastcgi.conf;
    }

    location ~ /\.ht {
        deny all;
    }
}
```

---

## 3. Database & MySQL User Setup

Run the following SQL commands to configure the production database:
```sql
CREATE DATABASE amanasuite CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'amanasuite'@'localhost' IDENTIFIED BY 'your_secure_password';
GRANT ALL PRIVILEGES ON amanasuite.* TO 'amanasuite'@'localhost';
FLUSH PRIVILEGES;
```
*(Note: Avoid using `#` or special characters in MySQL passwords to prevent PDO connection string errors).*

---

## 4. File Permissions & Security Setup

Execute these commands to ensure proper file permissions and prevent 500 errors:
```bash
cd /www/wwwroot/amanasuite.com

# Core permissions
chmod 755 .env
chmod -R 775 storage
chmod -R 775 bootstrap/cache
chmod -R 775 storage/logs

# Ownership for Nginx/PHP-FPM
chown -R www:www /www/wwwroot/amanasuite.com
```

---

## 5. SSL Certificate Configuration (Certbot / Let's Encrypt)
HTTPS is mandatory for API communication with mobile apps.

```bash
sudo certbot --nginx -d amanasuite.com -d www.amanasuite.com
```

To test automatic renewal:
```bash
sudo certbot renew --dry-run
```
