# Amana Mart React / Next.js Web Portal — Build & Production Deployment Guide

## 1. Production Architecture Overview
The **Amana Mart Customer Web Portal** (`amanamart.com`) is deployed at `/www/wwwroot/amanamart` as a Node.js production daemon managed by **PM2** and reverse-proxied by **Nginx SSL**.

---

## 2. Nginx Reverse Proxy Configuration (`amanamart.com`)

In `/www/server/panel/vhost/nginx/amanamart.com.conf`:

```nginx
server {
    listen 80;
    listen 443 ssl http2;
    server_name amanamart.com www.amanamart.com;

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
        proxy_cache_bypass $http_upgrade;
    }
}
```

---

## 3. Step-by-Step Production Build & Deployment

### Step 1: Install Dependencies & Build Next.js Production Assets
```bash
cd /www/wwwroot/amanamart
npm install
npm run build
```

### Step 2: PM2 Process Launch & Management
Launch the Next.js production server with PM2 under the process name `amanamart`:

```bash
cd /www/wwwroot/amanamart
pm2 start npm --name "amanamart" -- start
pm2 save
```

### Step 3: Useful PM2 Management Commands
- **Restart Web Portal:** `pm2 restart amanamart`
- **View Live Logs:** `pm2 logs amanamart`
- **Check Status & RAM:** `pm2 status amanamart`

---

## 4. Automated 1-Click Deployment Script (`scripts/build-react-web.sh`)

Run the automated deployment script:
```bash
/root/amana-mart-master-skill/scripts/build-react-web.sh
```
This script cleans the `.next` cache, compiles Next.js production assets, restarts PM2, and verifies HTTP 200 status on `https://amanamart.com`.
