---
name: amana-mart-master-skill
description: "Ultimate Master Skill, Interactive HTML Documentation, Developer CLI (amana), and Automation Suite for Amana Mart Multi-Vendor Ecosystem."
version: 2.5.0
author: Amana Agent, Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [amana-mart, amanasuite, flutter, nextjs, laravel, multi-vendor, e-commerce, interactive-docs, amana-cli]
---

# Amana Mart Ultimate Master Skill & Developer Suite (v2.5.0)

## Overview

This is the **Ultimate Master Skill and Developer Suite** for the **Amana Mart Ecosystem**. It provides a 100% self-contained master documentation architecture, interactive dual-language HTML portal (`index.html`), a dedicated Developer & Server Management CLI (`amana`), automated build scripts (`scripts/`), and complete configuration rules for Hermes Agent, MCP, and external CLI agents.

---

## ⚡ Amana Developer CLI (`amana`)

The ecosystem includes a native terminal CLI tool `amana` installed at `/usr/local/bin/amana` for instant server health checks, builds, and maintenance:

- **Check System Health & API Status:** `amana status`
- **Rebuild Next.js Web Portal:** `amana build web`
- **Build Customer App Release APK & Sync Drive:** `amana build user-app`
- **Build Delivery Driver App Release APK:** `amana build driver-app`
- **Build Store Merchant App Release APK:** `amana build vendor-app`
- **Clean System Logs & Optimize Disk:** `amana clean`
- **View Master Skill & Docs:** `amana docs`

---

## 🐙 Master GitHub Repositories Catalog

| Ecosystem Component | Purpose | GitHub Repository URL | Server / Local Directory |
| :--- | :--- | :--- | :--- |
| **Master Skill & Documentation** | Central Skill, Docs & Developer CLI | [amana-mart-master-skill](https://github.com/mahmudulhassan-dev/amana-mart-master-skill) | `/root/amana-mart-master-skill` |
| **Backend API & Admin Panel** | Laravel 11/12 Multi-Vendor Engine | `git@github.com:amanasuite/Amanasuite.git`<br>[amanamart-admin](https://github.com/mahmudulhassan-dev/amanamart-admin) | `/www/wwwroot/amanasuite.com` |
| **React Web Portal** | Next.js 15 Customer Storefront | [amanamart-web](https://github.com/mahmudulhassan-dev/amanamart-web) | `/www/wwwroot/amanamart` |
| **Customer Mobile App** | Flutter Customer App | `git@github.com:mahmudulhassan-dev/amanamart-user-app.git` | `/www/wwwroot/amanamartuserapp` |
| **Deliveryman Driver App** | Flutter GPS Tracking Driver App | `git@github.com:mahmudulhassan-dev/amanamart-deliveryman-app.git` | `/www/wwwroot/amanamartdeliverymanapp` |
| **Store Merchant App** | Flutter Vendor & Inventory App | `git@github.com:mahmudulhassan-dev/amanamart-vendor-app.git` | `/www/wwwroot/amanamartvendorapp` |

---

## 🏛️ Ecosystem Component Map & Paths

| Component | Technology | Server Directory / Domain | Local Documentation File |
| :--- | :--- | :--- | :--- |
| **Interactive HTML Portal** | HTML5 / CSS3 / JS | `/root/amana-mart-master-skill/index.html` | Open `index.html` in browser for English & Bengali interactive UI |
| **Developer CLI Tool** | Python 3 / Bash | `/usr/local/bin/amana` | `scripts/amana-cli.py` |
| **Backend & Admin Panel** | Laravel / PHP 8.2 | `/www/wwwroot/amanasuite.com`<br>`https://amanasuite.com` | `docs/02-admin-installation.md`<br>`docs/10-aapanel-and-vps-deployment-guide.md` |
| **Frontend Web App** | Next.js 15 / React 18 | `/www/wwwroot/amanamart`<br>`https://amanamart.com` | `docs/06-react-web-build-deploy.md`<br>`docs/06-react-web-mandatory-web.md` |
| **Customer User App** | Flutter 3.x / Dart | `/www/wwwroot/amanamartuserapp` | `docs/03-user-app-mandatory-setup.md`<br>`docs/03-user-app-build-release.md` |
| **Deliveryman App** | Flutter 3.x / Dart | `/www/wwwroot/amanamartdeliverymanapp` | `docs/04-deliveryman-driver-app-setup-and-build-guide.md` |
| **Store / Vendor App** | Flutter 3.x / Dart | `/www/wwwroot/amanamartvendorapp` | `docs/05-vendor-app-mandatory-setup.md` |

---

## 🎨 Amana Mart Brand Specifications

- **Primary Neon Mint:** `#10F3A2`
- **Secondary Cyan Blue:** `#33B5FF`
- **Background Pitch Black:** `#0B0E14`
- **Surface Dark Card:** `#121722`
- **Border Charcoal:** `#232D3F`
- **Typography:** `Plus Jakarta Sans`, `DMSans`, `Noto Sans Bengali`

---

## 🔒 Mandatory Safety & Version Control Rules

1. **Explicit Permission Required:** Always ask for explicit user permission before modifying server code, Nginx configs, or DB tables.
2. **Git Version Control:** Commit and push all web or admin code changes to `mahmudulhassan-dev/amanamart-web` or `amanamart-admin`.
3. **Google Drive Sync:** Sync major APK builds and documentation updates to `google drive:All Web Site/Amana Mart/`.
