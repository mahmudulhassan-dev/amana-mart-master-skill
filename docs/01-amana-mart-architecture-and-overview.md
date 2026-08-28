# Amana Mart Ecosystem — Architecture & Overview

## 1. System Overview
Amana Mart is an enterprise multi-vendor eCommerce and hyperlocal delivery platform consisting of 5 main operational pillars:
1. **Laravel Backend & Admin Panel** (`https://amanasuite.com`): Central Database, Multi-Vendor Admin, Store Merchant Management, Finance & Commission System.
2. **Next.js Web Portal** (`https://amanamart.com`): High-speed customer web storefront supporting English and Bengali languages.
3. **Customer User App** (Flutter): Android and iOS mobile app for customer shopping, order placement, and live tracking.
4. **Deliveryman Driver App** (Flutter): Mobile app for delivery drivers, location tracking, and order fulfillment.
5. **Store / Vendor App** (Flutter): Mobile app for store owners to manage products, accept orders, and view earnings.

## 2. Technology Stack Specifications
- **Backend & Admin Panel:** Laravel 11 / PHP 8.2+ / MySQL 8.0 / MariaDB 10.6+ / Redis / Pusher Reverb
- **Web Frontend:** Next.js 15 / React 18 / Material-UI / i18next (English & Bengali)
- **Mobile Applications:** Flutter 3.x / Dart / Android SDK (API 31-36) / Java 17
- **Server Infrastructure:** Ubuntu 24.04 LTS / aaPanel / Docker Compose / Nginx / PM2 / Cloudflare R2 / S3
