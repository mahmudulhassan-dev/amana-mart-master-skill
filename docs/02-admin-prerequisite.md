# Amana Suite Admin Panel & Backend Prerequisites Guide

## 1. Server Environment Specifications
To run the **Amana Suite Backend & Admin Panel** (`https://amanasuite.com`) with optimal security and high concurrency, your server environment must meet the following prerequisites:

- **Operating System:** Ubuntu 24.04 LTS (64-bit) / Linux Server
- **PHP Engine:** PHP 8.2 or PHP 8.3
- **Database:** MySQL 8.0 or MariaDB 10.6+
- **Web Server:** Nginx 1.24+ with SSL (HTTPS)
- **Control Panel:** aaPanel / BT-Panel or Native Linux Terminal

---

## 2. Mandatory PHP Extensions Checklist

The following 14 PHP extensions are mandatory for **Amana Suite** to function properly (API authentication, image processing, JWT tokens, and encrypted payments):

1. **`mod_rewrite`** — URL rewrites and Nginx location blocks
2. **`bcmath`** — Arbitrary precision math for financial commission calculations
3. **`ctype`** — Character type checking
4. **`fileinfo`** — File upload MIME type verification
5. **`gd`** / **`imagick`** — Image compression, thumbnail generation, and watermarking
6. **`json`** — API JSON response encoding and parsing
7. **`mbstring`** — Multibyte string processing (essential for Bengali unicode text)
8. **`openssl`** — Encrypted HTTPS communication and JWT token generation
9. **`pdo`** & **`pdo_mysql`** — Database connection driver
10. **`sodium`** — Cryptographic operations
11. **`tokenizer`** — PHP source code token parsing
12. **`xml`** — XML data parsing
13. **`zip`** — Backup archive compression and extraction
14. **`curl`** — External HTTP requests to payment, SMS, and FCM gateways

---

## 3. Verifying PHP Extensions on Server

Run the following command in terminal to verify all required PHP extensions are active on `/www/wwwroot/amanasuite.com`:

```bash
php -m | grep -iE "bcmath|ctype|curl|fileinfo|gd|json|mbstring|openssl|pdo_mysql|sodium|tokenizer|xml|zip"
```

If any extension is missing on aaPanel:
1. Open aaPanel > **App Store** > **PHP 8.2 / 8.3**.
2. Click **Install Extension** and activate the missing module (`bcmath`, `fileinfo`, `gd`, `sodium`, etc.).
