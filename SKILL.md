---
name: amana-mart-master-skill
description: "Master Skill & Complete Documentation Guide for Amana Mart Multi-Vendor Ecosystem (Laravel Backend, Next.js Web, Flutter Apps)."
version: 1.0.0
author: Amana Agent, Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [amana-mart, 6ammart, flutter, nextjs, laravel, multi-vendor, e-commerce]
---

# Amana Mart Master Skill & Documentation Architecture

## Overview

This is the Master Skill for the **Amana Mart Ecosystem**. It provides complete technical context, file paths, build workflows, language configuration rules, and troubleshooting procedures for Hermes Agent, MCP, and external CLI agents working on any component of Amana Mart.

---

## Ecosystem Component Map & Paths

| Component | Technology | Server Directory / Domain | Purpose |
| :--- | :--- | :--- | :--- |
| **Backend & Admin Panel** | Laravel / PHP 8.2 | `/www/wwwroot/amanasuite.com`<br>`https://amanasuite.com` | Central API, Database, Multi-Vendor Admin & Store Panel |
| **Frontend Web App** | Next.js 15 / React 18 | `/www/wwwroot/amanamart`<br>`https://amanamart.com` | Customer Web Portal, Order Checkout, Store Directory |
| **Customer User App** | Flutter 3.x / Dart | `/www/wwwroot/amanamartuserapp` | Android & iOS App for Customers |
| **Deliveryman App** | Flutter 3.x / Dart | `/www/wwwroot/amanamartdeliverymanapp` | Android & iOS App for Delivery Drivers & Order Tracking |
| **Store / Vendor App** | Flutter 3.x / Dart | `/www/wwwroot/amanamartvendorapp` | Android & iOS App for Store Merchants & Managers |

---

## 1. Customer Web Portal Configuration (`amanamart.com`)

### Language Configuration Rules
- **Supported Languages:** English (`en`) and Bengali (`bn`) ONLY.
- **Translation File Locations:**
  - `/www/wwwroot/amanamart/src/language/en.js` (English strings)
  - `/www/wwwroot/amanamart/src/language/bn.js` (Bengali strings)
  - `/www/wwwroot/amanamart/src/language/i18n.js` (i18next config)
  - `/www/wwwroot/amanamart/src/components/header/top-navbar/language/languageList.js` (English & Bengali flag definitions)
- **CRITICAL:** All 2,500+ keys in `bn.js` MUST contain authentic Bengali translations. If `bn.js` keys contain English text, switching to Bengali will show English UI strings.
- **Build & Restart Command:**
  ```bash
  cd /www/wwwroot/amanamart
  npm run build
  pm2 restart amanamart
  ```

---

## 2. Customer User App Configuration (`amanamartuserapp`)

### Essential App Constants (`lib/util/app_constants.dart`)
```dart
class AppConstants {
  static const String appName = 'Amana Mart';
  static const String webHostedUrl = 'https://amanamart.com';
  static const String baseUrl = 'https://amanasuite.com';
  // ...
}
```

### Android Build Environment
- **Flutter Path:** `/opt/flutter/bin/flutter`
- **Android SDK Path:** `/opt/android-sdk`
- **Required Platform SDKs:** `platforms;android-31`, `platforms;android-33`, `platforms;android-34`, `platforms;android-35`
- **Gradle Heap Limit (`android/gradle.properties`):**
  ```properties
  org.gradle.jvmargs=-Xmx3072m -XX:MaxMetaspaceSize=1024m -XX:ReservedCodeCacheSize=512m -XX:+HeapDumpOnOutOfMemoryError
  ```
- **Crashlytics Release Note:** If Google Services JSON lacks active Crashlytics project ID, disable `com.google.firebase.crashlytics` in `android/app/build.gradle.kts`.

### APK Build Command
```bash
export ANDROID_HOME=/opt/android-sdk
cd /www/wwwroot/amanamartuserapp
/opt/flutter/bin/flutter build apk --release
```
**Compiled Output:** `/www/wwwroot/amanamartuserapp/build/app/outputs/flutter-apk/app-release.apk`

---

## 3. GitHub Repository & Skill Backup

Full documentation and master skill assets are maintained at:
- **Local Directory:** `/root/amana-mart-master-skill`
- **Skills Directory:** `/root/.hermes/skills/amana-mart-master-skill`
- **GitHub Target Repo:** `mahmudulhassan-dev/amana-mart-master-skill`

---

## 4. Safety & Approval Rules (Mandatory)

1. **User Approval First:** Always request explicit permission before making permanent changes to server code, database tables, or Nginx configurations.
2. **Commit & Push Version Control:** Any code or configuration changes on Amana Mart web or admin MUST be committed and pushed to their GitHub repositories (`amanamart-web` or `amanamart-admin`).
3. **Google Drive Backup Sync:** Upload compiled APKs and major documentation releases to `google drive:All Web Site/Amana Mart/`.
