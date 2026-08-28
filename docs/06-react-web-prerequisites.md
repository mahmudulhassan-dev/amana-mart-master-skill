# Amana Mart React / Next.js Web Portal — Prerequisites Guide

## 1. Application Overview & Path
The **Amana Mart Customer Web Portal** is built using **Next.js 15** and **React 18** to deliver a high-speed, SEO-optimized e-commerce storefront supporting **English and Bengali** languages.

- **Server Path:** `/www/wwwroot/amanamart`
- **Live Domain:** `https://amanamart.com`
- **Backend API Host:** `https://amanasuite.com`

---

## 2. Server Infrastructure & Tooling Prerequisites

| Component / Tool | Required Version | Server / Workstation Path |
| :--- | :--- | :--- |
| **Node.js Engine** | Node.js v20+ / v22+ (Active LTS) | `/usr/bin/node` |
| **Package Manager** | npm v10+ / pnpm / yarn | `/usr/bin/npm` |
| **Process Manager** | PM2 (`pm2`) | `/usr/bin/pm2` |
| **Web Server** | Nginx 1.24+ SSL (Reverse Proxy) | `/etc/nginx/` / aaPanel |
| **Operating System** | Ubuntu 24.04 LTS | VPS Server (`148.230.98.190`) |

---

## 3. Verifying Node & PM2 Readiness

Run the following commands on the server to verify Next.js deployment tools:

```bash
node -v
npm -v
pm2 -v
```

Expected node version: `v20.x.x` or `v22.x.x`.
