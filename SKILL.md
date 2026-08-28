---
name: amana-mart-master-skill
description: "Offline Master Skill & Comprehensive Documentation Index for Amana Mart Ecosystem (Laravel, Next.js, Flutter User/Delivery/Vendor Apps)."
version: 1.1.0
author: Amana Agent, Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [amana-mart, 6ammart, flutter, nextjs, laravel, multi-vendor, e-commerce, offline-docs]
---

# Amana Mart Offline Master Skill & Complete Documentation Index

## Overview

This Master Skill provides **100% offline, self-contained technical documentation and operational rules** for the **Amana Mart Ecosystem**. All documentation text, installation steps, API parameters, and build commands are cloned directly inside this repository—**no external URLs or external websites required**.

---

## 🏗️ Ecosystem Component Map & Paths

| Component | Technology | Server Path / Domain | Local Documentation File |
| :--- | :--- | :--- | :--- |
| **Backend & Admin Panel** | Laravel / PHP 8.2 | `/www/wwwroot/amanasuite.com`<br>`https://amanasuite.com` | `docs/02-admin-installation.md`<br>`docs/02-admin-local-config.md` |
| **Frontend Web App** | Next.js 15 / React 18 | `/www/wwwroot/amanamart`<br>`https://amanamart.com` | `docs/06-react-web-build-deploy.md`<br>`docs/06-react-web-mandatory-web.md` |
| **Customer User App** | Flutter 3.x / Dart | `/www/wwwroot/amanamartuserapp` | `docs/03-user-app-mandatory-setup.md`<br>`docs/03-user-app-build-release.md` |
| **Deliveryman App** | Flutter 3.x / Dart | `/www/wwwroot/amanamartdeliverymanapp` | `docs/04-delivery-app-mandatory-setup.md`<br>`docs/04-delivery-app-build-release.md` |
| **Store / Vendor App** | Flutter 3.x / Dart | `/www/wwwroot/amanamartvendorapp` | `docs/05-vendor-app-mandatory-setup.md`<br>`docs/05-vendor-app-build-release.md` |

---

## 📂 Offline Local Documentation Catalog (`/docs/`)

### 1. System Overview & Architecture
- `docs/01-overview-intro.md` — 6amMart Ecosystem Architecture & Multi-Vendor Overview.
- `docs/01-overview-summary.md` — System Requirements, Stack Specifications & Database Relationships.

### 2. Admin Panel & Laravel Backend Configuration
- `docs/02-admin-prerequisites.md` — Server Requirements (PHP 8.2, MySQL 8, Extensions).
- `docs/02-admin-installation.md` — Step-by-Step Laravel Installation & Database Import.
- `docs/02-admin-local-config.md` — `.env` Settings, Database Credentials & Cron Job Setup.
- `docs/02-admin-mandatory-setups.md` — Business Settings, Payment Gateways, SMS & Mail Gateways.
- `docs/02-admin-3rd-party.md` — Google Maps API, Firebase FCM Server Keys, Recaptcha Setup.
- `docs/02-admin-customization.md` — Customizing Branding, Colors, Logos & Mail Templates.
- `docs/02-admin-rental-module.md` — Car Rental Module Add-on Installation & Configuration.
- `docs/02-admin-vendor-website-builder.md` — Vendor Website Builder Add-on Setup.

### 3. Customer Mobile Application (Flutter)
- `docs/03-user-app-prerequisites.md` — Flutter 3.x, Dart, Android Studio & Xcode Environment.
- `docs/03-user-app-environment.md` — Package Name, App Title & `lib/util/app_constants.dart` Configuration.
- `docs/03-user-app-mandatory-setup.md` — Connecting App to Backend API (`https://amanasuite.com`).
- `docs/03-user-app-3rd-party.md` — Firebase FCM, Google Maps, Social Login (Google/Facebook/Apple).
- `docs/03-user-app-build-release.md` — Android Release APK & AAB Compilation Guidelines.
- `docs/03-user-app-customization.md` — UI Color Palette, Fonts, Splash Screen & Asset Icons.
- `docs/03-user-app-system-update.md` — Upgrading Customer App Version & Migrating Dependencies.
- `docs/03-user-app-rental-addon.md` — Car Rental Feature Integration in Customer App.

### 4. Deliveryman Mobile Application (Flutter)
- `docs/04-delivery-app-prerequisites.md` — Flutter Environment & Mobile Requirements for Drivers.
- `docs/04-delivery-app-environment.md` — App ID & Constants Setup for Delivery App.
- `docs/04-delivery-app-mandatory-setup.md` — Background Location Tracking & Order Dispatch Setup.
- `docs/04-delivery-app-build-release.md` — Compiling Deliveryman APK & Play Store Release.
- `docs/04-delivery-app-customization.md` — Customizing Driver App Branding & Notification Sounds.
- `docs/04-delivery-app-system-update.md` — Version Upgrades for Deliveryman App.

### 5. Vendor / Store Provider Application (Flutter)
- `docs/05-vendor-app-prerequisites.md` — Prerequisites for Store Merchant App.
- `docs/05-vendor-app-environment.md` — Environment & API Endpoint Binding for Merchant App.
- `docs/05-vendor-app-mandatory-setup.md` — Product Management, Store Orders & Wallet Cashout.
- `docs/05-vendor-app-build-release.md` — Building Vendor APK & Play Store Distribution.
- `docs/05-vendor-app-customization.md` — Store App Branding & Notification Setup.
- `docs/05-vendor-app-system-update.md` — Merchant App Version Upgrades.
- `docs/05-vendor-app-rental-addon.md` — Vehicle Fleet & Car Rental Provider Setup.

### 6. React Web Portal (Next.js 15)
- `docs/06-react-web-prerequisites.md` — Node.js v20+, npm/pnpm, Next.js Prerequisites.
- `docs/06-react-web-environment.md` — `.env.production` Environment Variables & API Binding.
- `docs/06-react-web-mandatory-admin.md` — Admin Panel Web Settings & Domain Authorization.
- `docs/06-react-web-mandatory-web.md` — i18n Translation Rules (**English + Bengali Only**).
- `docs/06-react-web-build-deploy.md` — `npm run build` Optimization & PM2 Deployment.
- `docs/06-react-web-customization.md` — Material-UI Theme Customization & Bangladesh Flag Setup.
- `docs/06-react-web-rental-addon.md` — Car Rental Web Portal UI Setup.

### 7. System Version Updates & Maintenance
- `docs/07-update-admin-panel.md` — Upgrading Laravel Backend System Files & DB Migrations.
- `docs/07-update-mobile-apps.md` — Upgrading Flutter Apps Across Versions.
- `docs/07-update-react-web.md` — Upgrading Next.js Web App Packages & Dependencies.

### 8. Troubleshooting & Typical Issues
- `docs/08-troubleshooting-typical-issues.md` — 500 Server Errors, CORS Issues, Maps Key Errors, Translation Missing Fixes & Build Exceptions.

---

## 🛠️ Key Execution Workflows for Hermes Agent

### Rebuilding & Deploying Web Frontend
```bash
cd /www/wwwroot/amanamart
npm run build
pm2 restart amanamart
```

### Compiling Customer App APK
```bash
export ANDROID_HOME=/opt/android-sdk
cd /www/wwwroot/amanamartuserapp
/opt/flutter/bin/flutter build apk --release
```

---

## 🔒 Mandatory Safety Rules

1. **Explicit Permission Required:** Always ask for explicit user permission before modifying server code, Nginx configs, or DB tables.
2. **Git Version Control:** Commit and push all web or admin code changes to `mahmudulhassan-dev/amanamart-web` or `amanamart-admin`.
3. **Google Drive Sync:** Sync major APK builds to `google drive:All Web Site/Amana Mart/`.
