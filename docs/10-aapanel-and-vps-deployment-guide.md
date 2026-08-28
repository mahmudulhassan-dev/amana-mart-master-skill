# Amana Mart Ecosystem — aaPanel & Ubuntu 24.04 VPS Deployment Guide

## 1. VPS Server Specifications & Overview
- **Operating System:** Ubuntu 24.04 LTS (64-bit)
- **Public IP:** `148.230.98.190`
- **Control Panel:** aaPanel v7.x (BT-Panel)
- **Primary Domain (Web):** `https://amanamart.com` (Directory: `/www/wwwroot/amanamart`)
- **Central API Domain (Backend):** `https://amanasuite.com` (Directory: `/www/wwwroot/amanasuite.com`)

---

## 2. aaPanel App Store Environment Setup

Ensure the following stack components are installed and active in aaPanel **App Store**:

1. **Nginx 1.24+:** Primary Web Server & Reverse Proxy with SSL (Let's Encrypt / Certbot).
2. **PHP 8.2 / PHP 8.3:** Active PHP engine with `bcmath`, `fileinfo`, `gd`, `sodium`, `zip`, `pdo_mysql`.
3. **MySQL 8.0 / MariaDB 10.6+:** Relational Database Engine.
4. **Redis 7.x:** In-memory caching for Laravel & Next.js session management.
5. **PM2 Manager:** Process Manager for Next.js Web Daemon & Laravel Reverb WebSockets.

---

## 3. aaPanel Nginx Site Configuration (`amanasuite.com`)

In aaPanel > **Website > amanasuite.com > Configuration**:

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

## 4. aaPanel Nginx Site Configuration (`amanamart.com`)

In aaPanel > **Website > amanamart.com > Configuration**:

```nginx
server {
    listen 80;
    listen 443 ssl http2;
    server_name amanamart.com *.amanamart.com;

    client_max_body_size 128M;

    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

---

## 5. Automated Backup Sync to Google Drive
The server automatically backs up databases and site files daily at 3:00 AM via `/www/backups/full_server_backup.sh` and syncs to:
`google drive:All Web Site/<Site_Name>/backup/` (SQL, File, Env).
