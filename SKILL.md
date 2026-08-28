---
name: amana-mart-master-skill
description: "Ultimate Master Skill, Interactive HTML Documentation, and Automation Suite for Amana Mart Multi-Vendor Ecosystem."
version: 2.0.0
author: Amana Agent, Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [amana-mart, 6ammart, flutter, nextjs, laravel, multi-vendor, e-commerce, interactive-docs]
---

# Amana Mart Ultimate Master Skill & Interactive Portal (v2.0.0)

## Overview

This is the **Ultimate Master Skill and Documentation Suite** for the **Amana Mart Ecosystem**. It provides a 100% self-contained, offline-ready master documentation architecture, interactive dual-language HTML portal (`index.html`), automated build scripts (`scripts/`), and complete configuration rules for Hermes Agent, MCP, and external CLI agents.

---

## 🏛️ Ecosystem Component Map & Paths

| Component | Technology | Server Directory / Domain | Local Documentation File |
| :--- | :--- | :--- | :--- |
| **Interactive HTML Portal** | HTML5 / CSS3 / JS | `/root/amana-mart-master-skill/index.html` | Open `index.html` in browser for English & Bengali interactive UI |
| **Backend & Admin Panel** | Laravel / PHP 8.2 | `/www/wwwroot/amanasuite.com`<br>`https://amanasuite.com` | `docs/02-admin-installation.md`<br>`docs/02-admin-local-config.md` |
| **Frontend Web App** | Next.js 15 / React 18 | `/www/wwwroot/amanamart`<br>`https://amanamart.com` | `docs/06-react-web-build-deploy.md`<br>`docs/06-react-web-mandatory-web.md` |
| **Customer User App** | Flutter 3.x / Dart | `/www/wwwroot/amanamartuserapp` | `docs/03-user-app-mandatory-setup.md`<br>`docs/03-user-app-build-release.md` |
| **Deliveryman App** | Flutter 3.x / Dart | `/www/wwwroot/amanamartdeliverymanapp` | `docs/04-delivery-app-mandatory-setup.md`<br>`docs/04-delivery-app-build-release.md` |
| **Store / Vendor App** | Flutter 3.x / Dart | `/www/wwwroot/amanamartvendorapp` | `docs/05-vendor-app-mandatory-setup.md`<br>`docs/05-vendor-app-build-release.md` |

---

## 🎨 Amana Mart Brand Specifications

- **Primary Neon Mint:** `#10F3A2`
- **Secondary Cyan Blue:** `#33B5FF`
- **Background Pitch Black:** `#0B0E14`
- **Surface Dark Card:** `#121722`
- **Border Charcoal:** `#232D3F`
- **Typography:** `Plus Jakarta Sans`, `DMSans`, `Noto Sans Bengali`

---

## 🛠️ Automated Operations & Scripts (`/scripts/`)

- **`scripts/build-user-app.sh`**: One-click script to build Customer User App APK and sync to Google Drive.
- **`scripts/build-react-web.sh`**: Next.js production build and PM2 restart script.
- **`scripts/server-maintenance.sh`**: Automated log cleanup and server memory optimization script.

---

## 📂 Offline Local Documentation Catalog (`/docs/`)

- `docs/01-overview-intro.md` — 6amMart Ecosystem Architecture & Multi-Vendor Overview.
- `docs/01-overview-summary.md` — System Requirements & Database Relationships.
- `docs/02-admin-prerequisite.md` — Server Requirements (PHP 8.2, MySQL 8).
- `docs/02-admin-installation.md` — Step-by-Step Laravel Installation & Database Import.
- `docs/02-admin-local-config.md` — `.env` Settings, Database Credentials & Cron Setup.
- `docs/02-admin-mandatory-setups.md` — Business Settings, Payment Gateways & Mail Setup.
- `docs/02-admin-3rd-party.md` — Google Maps API, Firebase FCM Keys, Recaptcha.
- `docs/02-admin-customizations.md` — Branding, Logos, Colors & Mail Templates.
- `docs/02-admin-rental-module.md` — Car Rental Module Addon Installation.
- `docs/02-admin-vendor-website-builder.md` — Vendor Website Builder Setup.
- `docs/03-user-app-prerequisites.md` — Flutter 3.x, Android SDK & Xcode Setup.
- `docs/03-user-app-environment.md` — Package Name, App Title & Constants Setup.
- `docs/03-user-app-mandatory-setup.md` — Connecting App to Backend API (`https://amanasuite.com`).
- `docs/03-user-app-3rd-party.md` — Firebase FCM, Google Maps, Social Login.
- `docs/03-user-app-build-release.md` — Android Release APK & AAB Compilation.
- `docs/03-user-app-customization.md` — UI Colors, Fonts, Splash Screen & Asset Icons.
- `docs/03-user-app-system-update.md` — Customer App Version Upgrades.
- `docs/03-user-app-rental-addon.md` — Car Rental Feature Integration in Customer App.
- `docs/04-delivery-app-mandatory-setup.md` — Driver App Location & Tracking Setup.
- `docs/04-delivery-app-build-release.md` — Deliveryman APK Build & Play Store Release.
- `docs/05-vendor-app-mandatory-setup.md` — Store Product Management & Wallet Cashout.
- `docs/05-vendor-app-build-release.md` — Vendor App APK Build & Release.
- `docs/06-react-web-mandatory-web.md` — i18n Translation Rules (**English + Bengali Only**).
- `docs/06-react-web-build-deploy.md` — Next.js `npm run build` & PM2 Deployment.
- `docs/07-update-admin-panel.md` — System Version Updates.
- `docs/08-troubleshooting-typical-issues.md` — 500 Errors, CORS, Google Maps & Translation Fixes.

---

## 🔒 Mandatory Safety & Version Control Rules

1. **Explicit Permission Required:** Always ask for explicit user permission before modifying server code, Nginx configs, or DB tables.
2. **Git Version Control:** Commit and push all web or admin code changes to `mahmudulhassan-dev/amanamart-web` or `amanamart-admin`.
3. **Google Drive Sync:** Sync major APK builds and documentation updates to `google drive:All Web Site/Amana Mart/`.
