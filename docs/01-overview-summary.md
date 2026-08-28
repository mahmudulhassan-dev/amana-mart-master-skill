# Amana Mart Ecosystem — System Requirements & Deployment Architecture

## 1. System Requirements & Prerequisites (V4.1)

### A. Admin Panel & Backend (`amanasuite.com` - V4.1)
- **PHP Engine:** PHP 8.2 or PHP 8.3
- **Database:** MySQL 8.0 / MariaDB 10.6+
- **Framework:** Laravel 11 / 12
- **Required Extensions:** `bcmath`, `ctype`, `curl`, `fileinfo`, `json`, `mbstring`, `openssl`, `pdo_mysql`, `tokenizer`, `xml`, `zip`, `gd`
- **Server:** Ubuntu 24.04 LTS / Nginx / aaPanel

### B. Mobile Applications (Flutter V4.1)
- **SDK & Compiler:** Flutter SDK 3.x (Stable)
- **Java Runtime:** JDK 17 OpenJDK
- **Android SDK:** API Levels 31, 33, 34, 35, 36 (installed at `/opt/android-sdk`)
- **IDE:** Android Studio / VS Code
- **iOS Build:** Xcode 15+ / 16+ for IPA compilation

### C. React Web Portal (`amanamart.com` - V4.1)
- **Node Environment:** Node.js v20+ / v22+
- **Package Manager:** npm v10+ / pnpm
- **Framework:** Next.js 15 / React 18

---

## 2. White-Labeled Deployment Architecture

1. **Step 1: Admin Panel Deployment (`https://amanasuite.com`)**
   - Deploy the Laravel backend API on your remote server at `/www/wwwroot/amanasuite.com`.
   - The admin host URL (`https://amanasuite.com`) acts as the central **Base API URL** for all mobile apps and the web portal.

2. **Step 2: Customer Web Deployment (`https://amanamart.com`)**
   - Configure the Next.js web portal at `/www/wwwroot/amanamart` to connect to `https://amanasuite.com`.
   - Build and deploy to your primary domain `https://amanamart.com`.

3. **Step 3: Mobile Apps Configuration & Compilation**
   - Set `AppConstants.baseUrl = 'https://amanasuite.com'` and `AppConstants.appName = 'Amana Mart'` in the Customer, Driver, and Merchant Flutter mobile app repositories.
   - Compile Android Release APKs and iOS IPAs for distribution.
