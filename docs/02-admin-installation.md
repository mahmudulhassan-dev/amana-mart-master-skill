# Amana Suite Admin Panel Installation & Database Setup Guide

## 1. Installation Overview & Architecture Rules
The **Amana Suite Backend & Admin Panel** is hosted on its dedicated domain `https://amanasuite.com` (server directory `/www/wwwroot/amanasuite.com`).

### Critical Installation Rules:
1. **Subdomain Architecture:** Install the Admin Panel & API Backend on `https://amanasuite.com`. The customer web portal is hosted on `https://amanamart.com`.
2. **No Subdirectory Installation:** Never install the admin panel in a subfolder (e.g., `amanamart.com/admin`), as Next.js routing and CORS policies will break.
3. **Mandatory SSL (HTTPS):** HTTPS SSL certification must be active on `https://amanasuite.com` for mobile apps and web API traffic.

---

## 2. Step-by-Step Web Installation Wizard

### Step 1: File Upload & Permission Preparation
Upload the source zip to `/www/wwwroot/amanasuite.com` and extract it:
```bash
cd /www/wwwroot/amanasuite.com
unzip amanasuite-admin.zip
chmod 755 .env
chmod -R 775 storage bootstrap/cache
chown -R www:www /www/wwwroot/amanasuite.com
```

### Step 2: Launch Web Installer
Navigate to `https://amanasuite.com` in your web browser. The installation wizard will automatically start. Click **Get Started**.

### Step 3: PHP Extension & Permission Check
The system verifies all 14 mandatory PHP extensions (`bcmath`, `fileinfo`, `gd`, `mbstring`, `openssl`, `pdo_mysql`, etc.) and directory permissions. Click **Process Next** once verified.

### Step 4: License & Domain Activation
Provide the license activation details for `amanasuite.com` and click **Continue**.

### Step 5: Database Connection Setup
Enter your MySQL database credentials:
- **Database Host:** `127.0.0.1` (or `localhost`)
- **Database Name:** `amanasuite`
- **Database Username:** `amanasuite`
- **Database Password:** `your_secure_password`

### Step 6: Import SQL Database Schema
Click **Import Database** (or **Force Import Database** if re-installing) to execute initial table migrations and seed data.

### Step 7: Super Admin Account Creation
Set your primary Administrator credentials:
- **Admin Name:** `Mahmudul Hasan` / `Amana Admin`
- **Admin Email:** `admin@amanamart.com`
- **Admin Password:** `your_secure_admin_password`

Click **Complete Installation**.

---

## 3. Production Login Endpoints

- **Super Admin Login URL:** `https://amanasuite.com/login/admin`
- **Store / Merchant Panel Login URL:** `https://amanasuite.com/login/store`
