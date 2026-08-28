# Amana Mart Ecosystem — GitHub Repositories & Developer Map

## 1. Master Repository Catalog

To make onboarding and collaboration easy for developers and AI agents, the entire **Amana Mart Ecosystem** is mapped across dedicated GitHub repositories:

| Ecosystem Component | Purpose | GitHub Repository URL | Server / Local Directory |
| :--- | :--- | :--- | :--- |
| **Master Skill & Documentation** | Central Skill, Docs & Developer CLI | [amana-mart-master-skill](https://github.com/mahmudulhassan-dev/amana-mart-master-skill) | `/root/amana-mart-master-skill` |
| **Backend API & Admin Panel** | Laravel 11/12 Multi-Vendor Engine | `git@github.com:amanasuite/Amanasuite.git`<br>[amanamart-admin](https://github.com/mahmudulhassan-dev/amanamart-admin) | `/www/wwwroot/amanasuite.com` |
| **React Web Portal** | Next.js 15 Customer Storefront | [amanamart-web](https://github.com/mahmudulhassan-dev/amanamart-web) | `/www/wwwroot/amanamart` |
| **Customer Mobile App** | Flutter Customer App | `git@github.com:mahmudulhassan-dev/amanamart-user-app.git` | `/www/wwwroot/amanamartuserapp` |
| **Deliveryman Driver App** | Flutter GPS Tracking Driver App | `git@github.com:mahmudulhassan-dev/amanamart-deliveryman-app.git` | `/www/wwwroot/amanamartdeliverymanapp` |
| **Store Merchant App** | Flutter Vendor & Inventory App | `git@github.com:mahmudulhassan-dev/amanamart-vendor-app.git` | `/www/wwwroot/amanamartvendorapp` |

---

## 2. Amana CLI Tool (`amana`)

Developers can manage server health, builds, and maintenance directly from terminal using `amana`:

- **Check System Health & API Status:** `amana status`
- **Rebuild Next.js Web Portal:** `amana build web`
- **Build Customer App Release APK:** `amana build user-app`
- **Build Delivery Driver App Release APK:** `amana build driver-app`
- **Build Store Merchant App Release APK:** `amana build vendor-app`
- **Clean Server Logs & Optimize Disk:** `amana clean`
- **View Master Skill & Docs:** `amana docs`

---

## 3. Mandatory Development & Commit Guidelines

1. **Explicit Permission Required:** Always seek explicit user confirmation before modifying live server configurations, Nginx virtual hosts, or database schemas.
2. **Immediate Version Control Sync:** Any code modification on the server must be committed and pushed immediately to its respective GitHub repository.
3. **Google Drive Deployment Sync:** Major release APKs and documentation packages must be synced to Google Drive:
   - Path: `google drive:All Web Site/Amana Mart/`
