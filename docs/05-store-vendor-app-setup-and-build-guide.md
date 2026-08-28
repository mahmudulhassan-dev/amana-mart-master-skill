# Amana Mart Store / Vendor App Setup & Build Guide

## 1. Source Directory & Purpose
- **Source Directory:** `/www/wwwroot/amanamartvendorapp`
- **Purpose:** Store owners and merchants manage product listings, accept incoming orders, print invoices, and track daily sales.

## 2. Essential App Constants
- **App Name:** `Amana Mart Store`
- **Base API URL:** `https://amanasuite.com`

## 3. Build Command
```bash
export ANDROID_HOME=/opt/android-sdk
cd /www/wwwroot/amanamartvendorapp
/opt/flutter/bin/flutter build apk --release
```
